from django.urls import path
from . import views

# Defining URL patterns for web application.
app_name = 'myCV'
urlpatterns = [
    path('', views.myCV, name="my_CV"),
]
