from django import forms
from Warehouse.models import Material
from PeopleOnBoard.models import WorkPlace


class RequestForm(forms.Form):

    materials = forms.ModelMultipleChoiceField(queryset=Material.objects.all(),
                                               widget=forms.CheckboxSelectMultiple,
                                               required=True)
    materials.widget.attrs.update({'class': ''})

    origin = forms.ModelChoiceField(queryset=WorkPlace.objects.all(),
                                    empty_label='',
                                    required=True)
    origin.widget.attrs.update({'class': 'form-control',
                                'id': 'origin',
                                'autocomplete': 'off',
                                'placeholder': 'Origin of the order'})

    note = forms.CharField()


class ResponseForm(forms.Form):

    note = forms.CharField(max_length=500)




