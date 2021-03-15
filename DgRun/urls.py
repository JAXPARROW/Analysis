from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('clear', views.delete_all, name='delete_all'),
]