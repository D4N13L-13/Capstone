from django.urls import path
from . import views

app_name = 'myCV'
urlpatterns = [
    path('', views.myCV, name="my_CV"),
]
