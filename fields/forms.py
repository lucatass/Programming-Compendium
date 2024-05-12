from django import forms
from .models import Field, Tag
from datetime import datetime
from django.core.exceptions import ValidationError

class FieldForm(forms.Form):
    title_forms = forms.CharField()
    definition_forms = forms.CharField(widget=forms.Textarea)
    created_date_forms = forms.DateTimeField(initial=datetime.now, disabled=True)
                                             
    # Get all tags from the database to populate the dropdown
    tags = [(tag.id, tag.tag_name) for tag in Tag.objects.all()]
    tag_choices = forms.MultipleChoiceField(choices=tags, widget=forms.SelectMultiple())                                        

class TagForm(forms.Form):
    Tag_name = forms.ModelChoiceField(queryset=Tag.objects.all())
    