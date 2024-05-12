"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fields import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('', views.home_vw, name='home_url'),
    #path('field_create/', views.field_create_vw, name='field_create_url'),
    path('field_render/', views.field_render_vw, name='field_render_url'),
    path('vocabulary/', views.vocabulary_render_vw, name='vocabulary_url'),
    path('languages/', views.languages_render_vw, name='languages_url'),
    #path( 'add_field_with_tags/' , views.add_field_with_tags_vw, name='add_field_with_tags_url'),
    path('field_add/' , views.field_add_vw, name='field_add_url'),
    path('tag_select/', views.tag_select_vw, name='tag_select_url'),
    path('tag_definitions/<str:tag_name>/', views.tag_definitions_vw, name='tag_definitions_url'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)