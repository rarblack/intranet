from django import forms
from . import models


class UploadManyFiles(forms.ModelForm):

    class Meta:
        model = models.UploadFiles
        fields = ('file',)
