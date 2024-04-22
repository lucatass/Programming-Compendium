from django.shortcuts import render
from django.http import HttpResponse 
from .forms import FieldForm
from .models import Field, Tag
from datetime import datetime

# Create your views here.
def home_vw (request):
    latest_field = Field.objects.latest('created_date_md')
    total_additions = Field.objects.count()
    context = {
        'latest_addition': latest_field,
        'total_additions': total_additions,
    }
    


    return render(request,'home.html', context)

def field_create_vw(request):
    if request.method == 'POST':
        form_create = FieldForm(request.POST)
        if form_create.is_valid():
            form_title = form_create.cleaned_data['title_md']
            form_definition = form_create.cleaned_data['definition_md']
            
            
            form_field = Field.objects.create(
                title_md = form_title,
                definition_md = form_definition
                )
            form_field.save()
            return HttpResponse('form succesfully saved')
    form_create = FieldForm()
    return render(request, 'field_create.html', {'form_html': form_create})

def add_field_with_tags_vw(request):
    if request.method == 'POST':
        title_md = request.POST.get('title_md')
        definition_md = request.POST.get('definition_md')
        vocabulary_md = request.POST.get('vocabulary_md') == 'on'
        pragmatic_programmer_md = request.POST.get('pragmatic_programmer_md') == 'on'
        created_date_md = datetime.now()

        # Create the field
        field = Field.objects.create(
            title_md=title_md,
            definition_md=definition_md,
            vocabulary_md=vocabulary_md,
            pragmatic_programmer_md=pragmatic_programmer_md,
            created_date_md=created_date_md
        )

        # Add tags to the field
        tags_input = request.POST.get('tags', '')
        tags_list = [tag.strip() for tag in tags_input.split(',')]
        for tag_name in tags_list:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            field.tags.add(tag)

        return HttpResponse('/success/')  # Redirect to a success page
    else:
        # Handle GET request (e.g., render a form)
        return render(request, 'add_field_with_tags.html', {})



def field_render_vw(request):
    return render(request, 'field_render.html') 

def vocabulary_render_vw(request):
    fields_vocabulary = Field.objects.filter(vocabulary_md=True)
    return render(request, 'vocabulary.html',{'fields_html': fields_vocabulary})

def languages_render_vw(request):
    return render(request, 'languages.html')