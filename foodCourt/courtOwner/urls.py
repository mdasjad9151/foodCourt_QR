from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.sign_up, name='sign_up'),
    path('login/',views.log_in, name='login'),    
    path('profile/',views.user_profile, name='profile'),    
    path('logout/',views.log_out, name='logout'), 
    path('addcourtdetails/',views.addFoodCourt, name='addcourt'), 
]
