from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import FieldForm, TagForm
from .models import Field, Tag
from datetime import datetime
from django.shortcuts import get_object_or_404
# Create your views here.
def home_vw (request):
    latest_field = Field.objects.latest('created_date')
    total_additions = Field.objects.count()
    context = {
        'latest_addition': latest_field,
        'total_additions': total_additions,
    }
    return render(request,'home.html', context)


from .models import Field  # Import the Field model

def field_add_vw(request):
    if request.method =='POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title_forms']
            definition = form.cleaned_data['definition_forms']
            created_date = form.cleaned_data['created_date_forms']
            tags = form.cleaned_data.get('tags', [])
            tag_create = form.cleaned_data.get('tag_create', '')

            # Create a Field instance and save it to the database
            field = Field.objects.create(
                title=title,
                definition=definition,
                created_date=created_date,
            )
            field.tags.set(tags)  # Add tags to the Field instance

            return redirect('vocabulary_url')
    else:
        form = FieldForm()
    return render(request, 'field_add.html', {'form': form})

def tag_select_vw(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag_name = form.cleaned_data['Tag_name']
            return redirect('tag_definitions_url', tag_name=tag_name)
    else:
        form = TagForm()
    return render(request, 'tag_select.html', {'form': form})

def tag_definitions_vw(request, tag_name = None):
    tag = None
    fields_with_tag = None
    form = TagForm()
    
    tag = Tag.objects.get(tag_name=tag_name)
    fields_with_tag = Field.objects.filter(tags=tag)

    return render(request, 'tag_definitions.html', {'tag': tag, 'fields_with_tag': fields_with_tag, 'form':form})


def field_render_vw(request):
    return render(request, 'field_render.html') 

def vocabulary_render_vw(request):
    fields_html = Field.objects.all()
    print(fields_html)
    return render(request, 'vocabulary.html',{'fields': fields_html})

def languages_render_vw(request):
    return render(request, 'languages.html')