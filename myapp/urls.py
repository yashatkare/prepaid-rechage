
from unicodedata import name
from django.urls import path,include
from .import views
urlpatterns =[
   path("",views.homepage,name="home"),
   path("plans/",views.plan,name="plans"),     #show the particular operator plans 
   path("plans_details/<int:pk>",views.plans_details,name="plans_details"),   
   path("recharge/",views.insertdata,name="recharge"),
   path("success/",views.success,name="success"),
 ]