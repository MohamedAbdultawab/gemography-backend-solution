from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_100_languages, name='list_100_languages'),
]