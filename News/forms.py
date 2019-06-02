from django import forms
from .models import Article


class ArticleCreateModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['subject', 'title', 'importance', 'introduction', 'body', 'conclusion', 'tags']
        widgets = {
            'introduction': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'conclusion': forms.Textarea(attrs={'cols': 40, 'rows': 3})
        }


class ArticleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['subject', 'title', 'importance', 'introduction', 'body', 'conclusion', 'tags', 'primary_image', 'secondary_image']
        widgets = {
            'introduction': forms.Textarea(attrs={'cols': 40, 'rows': 2}),
            'body': forms.Textarea(attrs={'cols': 40, 'rows': 8}),
            'conclusion': forms.Textarea(attrs={'cols': 40, 'rows': 3})
        }

