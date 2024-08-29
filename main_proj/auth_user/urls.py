from django.urls import path
from . import views

# Defining URL patterns for web application.
# Each Path function call, specifies a URL pattern along with the
# corresponding view function that should be called
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
]
