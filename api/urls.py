from django.urls import path

from . import views

urlpatterns = [
    path('languages', views.list_trending_languages, name='list_trending_languages'),
]