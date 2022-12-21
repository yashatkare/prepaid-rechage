# from django.shortcuts import render
from email import message
from multiprocessing.sharedctypes import Value
from opcode import opname
from pickle import DICT
from django.shortcuts import redirect, render
from .models import *
# Create your views here.



def homepage(request):
    operators=list(operator.objects.values())  # type casting to list data type from queryset datatype
    context={}
    context["operators"]=operators
    return render(request,"app/home.html",context)



#  show operator plans 
def plan(request):
    operatorid=request.POST['operatorid']             #getting operator id from home page
    phonenumber=request.POST['phoneno']                #getting user phone number from home page
    all_data=plans.objects.filter(operator_id=operatorid)    #store all data of the particular operator plans using the operator id
    operatorname=operator.objects.get(id=operatorid).operator_name
    print(all_data,operatorid)
    return render(request,"app/show.html",{'key1':all_data,'key2':operatorid,'key3':phonenumber,'msg':operatorname})


def plans_details(request,pk): 
    phonenumber=request.POST['phoneno']               #getting user phone number from showpage
    operatorid=request.POST['operatorid']          #getting operator id from from showpage
    plandata=plans.objects.get(id=pk)               #getting plans of the using plan id
    return render(request,"app/recharge.html",{'key3':plandata,'key4':phonenumber,'key5':operatorid})

# insert data into the recharge table

def insertdata(request):
    phonenumber=request.POST['phoneno']          #getting user phone number from recharge page
    operatorid=request.POST['operatorid']        #getting user operatorid  from recharge page
    planid=request.POST['planid']                 #getting plan id from recharge page
    newdata= userrecharge.objects.create(phone_number=phonenumber, plan_id=planid, operator_id=operatorid)
    return redirect("success")

def success(request):
      message="recharge successfully"
      return render(request,"app/success.html",{'msg':message})    

# Create your views here.
