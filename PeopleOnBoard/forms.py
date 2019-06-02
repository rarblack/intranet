from django import forms
from .models import Employee, WorkPlace, EmployeeInstance, Profession, Transportation


class UpdateEmployeeInstanceForm(forms.Form):

    end_time = forms.DateTimeField(required=False)

    end_time.widget.attrs.update({'class': 'form-control',
                                  'id': 'end-time',
                                  'placeholder': 'End time'})


class AddEmployeeInstanceForm(forms.Form):
    employee = forms.ModelChoiceField(queryset=Employee.objects.filter(status__exact='a'),
                                      empty_label='Employee')

    assigned_work_place = forms.ModelChoiceField(queryset=WorkPlace.objects.all(),
                                                 empty_label='Work place')

    start_time = forms.DateTimeField(required=False)

    note = forms.CharField(required=False,)

    employee.widget.attrs.update({           'id':'employeeid',           'class': 'form-control'           ,                                                                             'placeholder': 'Employee name' })

    assigned_work_place.widget.attrs.update({'id':'assignedworkplaceid',  'class': 'form-control'           ,                                                                             'placeholder': 'Assigned work place'})
    # note.widget.attrs.update({               'id':'noteid',               'class': 'form-control'           ,                                                                             'placeholder': 'Additional note'})
    # start_time.widget.attrs.update({         'id':'starttimeid',          'class': 'form-control', 'autocomplete': 'off', 'readonly': 'readonly', 'view-toggle': 'datepicker', 'placeholder': 'Starts time'})


class SearchEmployeeInstanceForm(forms.Form):

    assigned_work_place = forms.ModelChoiceField(queryset=WorkPlace.objects.all(),
                                                 required=True,
                                                 empty_label='Work place')

    profession = forms.ModelChoiceField(queryset=Profession.objects.all(),
                                        required=True,
                                        empty_label='Profession')

    transport = forms.ModelChoiceField(queryset=Transportation.objects.all(),
                                       required=True,
                                       empty_label='Transport')

    company = forms.CharField(required=True)

    start_time = forms.DateTimeField(required=True)

    end_time = forms.DateField(required=True)

    work_id = forms.CharField(required=True)

    id_card = forms.CharField(required=True)

    assigned_work_place.widget.attrs.update({'id': 'assignedworkplaceid',
                                             'class': 'form-control col-md-3 mr-md-5 ml-md-5 col-lg-3 mr-lg-5 ml-lg-5',
                                             'placeholder': 'Assigned work place'})

    profession.widget.attrs.update({'id': 'professionid',
                                    'class': 'form-control col-md-3 mr-md-5 ml-md-5 col-lg-3 mr-lg-5 ml-lg-5',
                                    'placeholder': 'Profession'})

    transport.widget.attrs.update({'id': 'transportid',
                                   'class': 'form-control col-md-3 mr-md-5 col-lg-3 mr-lg-5',
                                   'placeholder': 'Transport'})
