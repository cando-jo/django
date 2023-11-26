from django.urls import path
import datetime
from . import views

urlpatterns = [
    path('', views.index, name="index")
]