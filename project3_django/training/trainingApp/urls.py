from . import views
from django.urls import path

urlpatterns = [
    path("<str:name>", views.welcome, name="welcome"),
]
