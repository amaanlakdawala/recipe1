from django.urls import path
from .views import *

urlpatterns = [  
    path('',success,name="home"),
    path('delete/<pk>/',delete,name="delete"),
     path('update/<pk>/',update,name="update"),
     path('login_page/',login_page,name='login_page'),
     path('register/',register, name='register'),
     path('logout_page/',logout_page,name='logout_page'),

]