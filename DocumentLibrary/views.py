from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect, Http404, HttpResponse
from Intranet import settings
import os
from . import forms
from .models import UploadFiles
import re

from News.functions import articles_latest, employees_closest_birthdays, employees_newest


class FileCreateView(generic.CreateView):
    model = UploadFiles
    fields = []
    template_name = 'doclib/partial/structure/upload-files.html'
    success_url = reverse_lazy('doclib:view-uploaded-files')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def form_valid(self, form):
        files = self.request.FILES.getlist('file')
        allowed_file_extensions = ['xls', 'doc', 'docx', 'pdf']
        for file in files:
            file_converted_to_string = str(file)
            file_regex = re.search(r"([a-zA-Z0-9-_\s]+?)[.](\w+?)$", file_converted_to_string)
            file_name, file_extension = file_regex.group(1), file_regex.group(2)
            if file_extension in allowed_file_extensions:
                self.object = form.save(commit=False)
                self.object.file = file
                self.object.file_name = file_name
                self.object.file_extension = file_extension
                self.object.belonged_department = self.request.user.profile.department
                self.object.created_by = self.request.user
                self.object.save()
        return super().form_valid(form)


# class FormUploadFilesView(generic.FormView):
#     form_class = forms.UploadManyFiles
#     template_name = 'doclib/partial/structure/upload-files.html'  # Replace with your template.
#     success_url = reverse_lazy('doclib:view-uploaded-files')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["latest_articles"] = articles_latest()
#         context["closest_birthdays"] = employees_closest_birthdays()
#         context["newest_employees"] = employees_newest()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         files = request.FILES.getlist('file')
#         allowed_file_extensions = ['xls', 'doc', 'docx', 'pdf']
#         if form.is_valid():
#             for file in files:
#                 file_converted_to_string = str(file)
#                 file_regex = re.search(r"([a-zA-Z0-9-_\s]+?)[.](\w+?)$", file_converted_to_string)
#                 file_name, file_extension = file_regex.group(1), file_regex.group(2)
#                 if file_extension in allowed_file_extensions:
#
#                     uploaded_file = form.save(commit=False)
#                     uploaded_file.file = file
#                     uploaded_file.file_name = file_name
#                     uploaded_file.file_extension = file_extension
#                     uploaded_file.belonged_department = request.user.profile.department
#                     uploaded_file.created_by = self.request.user
#                     uploaded_file.save()
#                 else:
#                     return self.form_invalid(form)
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)


class ListViewFilesView(generic.ListView):
    model = UploadFiles
    template_name = 'doclib/partial/structure/view-uploaded-files.html'
    context_object_name = 'documents'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def get_queryset(self):
        return self.model.objects.filter(belonged_department=self.request.user.profile.department)


class DeleteUploadFilesView(generic.DeleteView):
    model = UploadFiles
    success_url = reverse_lazy('doclib:view-uploaded-files')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_articles"] = articles_latest()
        context["closest_birthdays"] = employees_closest_birthdays()
        context["newest_employees"] = employees_newest()
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        os.remove(os.path.join(settings.MEDIA_ROOT, self.object.file.name))
        return HttpResponseRedirect(self.get_success_url())


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,
                             path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404
