from django.urls import path
from . import views

urlpatterns = [
    path('projects/all', views.APIProjectsList.as_view(), name='api'),
]

