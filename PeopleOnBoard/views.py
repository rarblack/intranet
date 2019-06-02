from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .models import EmployeeInstance, Employee
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
from .forms import AddEmployeeInstanceForm, SearchEmployeeInstanceForm
from django.utils import timezone


@permission_required('PeopleOnBoard.can_add_instance')
@login_required
def addEmployeeInstance(request):
    now = timezone.now()

    # If this is a POST request then process the Form view
    if request.method == 'POST':

        # Create a form instance and populate it with view from the request (binding):
        form = AddEmployeeInstanceForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            emp_inst = EmployeeInstance()

            emp_inst.assigned_work_place_object = form.cleaned_data['assigned_work_place']
            emp_inst.employee_object = form.cleaned_data['employee']

            if form.cleaned_data['start_time']:
                emp_inst.start_time = form.cleaned_data['start_time']
                #
                # if form.cleaned_data > 15:
                #     emp_inst.squad_order = '1'
                # else:
                #     emp_inst.squad_order = '2'

            else:
                emp_inst.start_time = now
                #
                # if now.day > 15:
                #     emp_inst.squad_order = '1'
                # else:
                #     emp_inst.squad_order = '2'

            emp_inst.note_name = form.cleaned_data['note']

            emp_inst.is_terminated = False
            emp_inst.assigner_object = request.user
            emp_inst.created_time = datetime.datetime.now()
            emp_inst.save()

            emp = get_object_or_404(Employee, pk=form.cleaned_data['employee'].pk)
            emp.status = 'r'
            emp.save()

            return HttpResponseRedirect(reverse('search'))

    # If this is a GET (or any other method) form the default form.
    else:
        form = AddEmployeeInstanceForm()

    context = {
        'form': form,
    }

    return render(request,
                  'pobapp/search.html',
                  context=context,)


@login_required()
def pob(request):
    emp = Employee

    if request.method == 'POST':
        form = SearchEmployeeInstanceForm(request.POST)
        formadd = AddEmployeeInstanceForm(request.POST)

        if form.is_valid():
            emp_inst = EmployeeInstance.objects.all()
            query_set = emp_inst.select_related('assigner_object', 'employee_object', 'assigned_work_place_object').filter(
                assigned_work_place_object_id__exact=form.cleaned_data['assigned_work_place'],
                employee_object__company_object__company_name__icontains=form.cleaned_data['company'],
                start_time__gte=form.cleaned_data['start_time'],
                end_time__lte=form.cleaned_data['end_time'],
                employee_object__profession_object_id__exact=form.cleaned_data['profession'],
                employee_object__work_id_card_name__icontains=form.cleaned_data['work_id'],
                employee_object__id_card_name__icontains=form.cleaned_data['id_card'],
                employee_object__transportation_object_id__exact=form.cleaned_data['transport']
            )

            context = {
                'query_set': query_set
            }
            return render(request,
                          'pobapp/table.html',
                          context)

    else:
        form = SearchEmployeeInstanceForm()
        formadd = AddEmployeeInstanceForm()

    emp_count_a = emp.objects.filter(status__exact='a')

    context = {
        'form': form,
        'formadd': formadd,
        'emp_count_a': emp_count_a
    }

    return render(request,
                  'pobapp/search.html',
                  context=context)


@login_required
def view_update(request):

    emp = EmployeeInstance.objects.filter(end_time=None)

    context = {
        'query_set': emp
    }

    return render(request,
                  'pobapp/update.html',
                  context=context)



@login_required
def view_table(request):
    return render(request, 'pobapp/table.html')


@permission_required('PeopleOnBoard.can_update_instance')
@login_required
def update_employee_instance(request, pk):
    if request.method == 'POST':
        now = timezone.now()

        emp_inst = get_object_or_404(EmployeeInstance, pk=pk)
        emp = get_object_or_404(Employee, pk=emp_inst.employee_object.pk)

        emp_inst.end_time = now
        emp_inst.is_terminated = True
        emp_inst.save()

        emp.status = 'a'
        emp.save()

    return HttpResponseRedirect(reverse('update'))