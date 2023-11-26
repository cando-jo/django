from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cando", views.cando, name="cando"),
    path("zataar", views.zataar, name="zataar"),
    path("<str:name>", views.greet, name="greet")
]