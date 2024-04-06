from django.urls import path
from .views import *

urlpatterns = [  
    path('',success,name="home"),
    path('delete/<pk>/',delete,name="delete"),
     path('update/<pk>/',update,name="update"),

]