from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, Http404, HttpResponse
import os
import re

from Intranet import settings
from .models import DocumentModel


class NavigationTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'document_library/document_library/template/navigation/navigation_template.html'


class DocumentCreateView(LoginRequiredMixin, generic.CreateView):
    model = DocumentModel
    fields = ['file']
    template_name = 'document_library/document_library/create/document_create.html'
    success_url = reverse_lazy('document_library:documents_list')

    def form_valid(self, form):
        files = self.request.FILES.getlist('file')
        allowed_file_extensions = ['xls', 'xlsx', 'doc', 'docx', 'pdf']
        counter = 0
        for file in files:
            file_converted_to_string = str(file)
            file_regex = re.search(r"([a-zA-Z0-9-_\s]+)[.](\w+?)$", file_converted_to_string)
            file_name, file_extension = file_regex.group(1), file_regex.group(2)
            if file_extension in allowed_file_extensions:
                self.model.objects.create(file=file,
                                          file_name=file_name,
                                          file_extension=file_extension,
                                          department_belonged=self.request.user.profile.department,
                                          creator=self.request.user)
                # self.object = form.save(commit=False)
                # self.object.file = file
                # self.object.file_name = file_name
                # self.object.file_extension = file_extension
                # self.object.department_belonged = self.request.user.profile.department
                # print(self.request.user.profile.department)
                # self.object.creator = self.request.user
                # self.object.save()
        return super().form_valid(form)


class DocumentsListView(LoginRequiredMixin, generic.ListView):
    model = DocumentModel
    template_name = 'document_library/document_library/list/documents_list.html'
    context_object_name = 'documents'

    def get_queryset(self):
        return self.model.objects.filter(department_belonged=self.request.user.profile.department).order_by('-creation_datetime')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table'] = self.kwargs.get('table')
        return context


class DeleteDocumentView(LoginRequiredMixin, generic.DeleteView):
    model = DocumentModel
    success_url = reverse_lazy('document_library:documents_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, self.object.file.name))
        return HttpResponseRedirect(self.get_success_url())


#                                                                                                                METHODS
def document_download_method(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,
                             path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
