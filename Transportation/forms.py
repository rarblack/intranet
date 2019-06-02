from django import forms
from .models import Car
from .choices import TRIP_TYPE


class RequestForm(forms.Form):

    car = forms.ModelChoiceField(queryset=Car.objects.all(),
                                 empty_label='')

    car.widget.attrs.update({'class': 'form-control'})

    trip_type = forms.ChoiceField(choices=TRIP_TYPE)

    trip_type.widget.attrs.update({'class': 'form-control'})

    origin = forms.CharField()

    destination = forms.CharField()

    leave_datetime = forms.CharField()

    return_datetime = forms.CharField()

    duration = forms.CharField()

    note = forms.CharField()


class ResponseForm(forms.Form):

    note = forms.CharField(max_length=500)


