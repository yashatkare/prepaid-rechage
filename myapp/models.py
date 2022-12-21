from django.db import models

# Create your models here.
class operator(models.Model):
    operator_name=models.CharField(max_length=50)

#recharge plans table
class plans(models.Model):
    operator_id=models.ForeignKey(operator,on_delete=models.CASCADE)   
    plans_name=models.CharField(max_length=50)
    amount=models.IntegerField()
    internet_data=models.CharField(max_length=50)
    call_hours=models.CharField(max_length=50)
    sms_data=models.CharField(max_length=50)

#used to save the data of recharge

class userrecharge(models.Model):
     plan_id=models.IntegerField()
     phone_number=models.BigIntegerField()
     operator_id=models.BigIntegerField()  
     recharge_date=models.DateTimeField(auto_now_add=True)
     activation_date=models.DateTimeField(auto_now_add=True)
