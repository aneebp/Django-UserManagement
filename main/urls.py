from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home,name='home'),
    path('home', views.Home,name='home'),
    path('register',views.Registration,name='register'),
    path('logout',views.Logout,name='logout'),


    
]