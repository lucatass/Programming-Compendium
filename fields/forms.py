from django import forms
from .models import Field

class FieldForm(forms.Form):
    title_forms = forms.CharField()
    definition_forms = forms.CharField(widget=forms.Textarea)
    vocabulary_forms = forms.BooleanField
    pragmatic_programmer_forms =  forms.BooleanField
    created_date_forms = forms.DateTimeField