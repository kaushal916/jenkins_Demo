#URLS for the app1

from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="homepage"),
    path('home', views.home2, name="homepage2"),
]