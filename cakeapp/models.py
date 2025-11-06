from django.db import models

# Create your models here.

class cakebelogin(models.Model):
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    
    class Meta():
        db_table="cakebelogin"
        
        
class cakebecakes(models.Model):
    cakename=models.CharField(max_length=50)
    caketype=models.CharField(max_length=50)
    cakeprice=models.CharField(max_length=50)
    cakequantity=models.CharField(max_length=50)
    cakeweight=models.CharField(max_length=50)
    cakephoto=models.FileField(max_length=100,upload_to='',blank=True,null=True)
    
    class Meta():
        db_table="cakebecakes"
