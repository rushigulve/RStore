from email.policy import default
from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50 ,default="")
    sub_category=models.CharField(max_length=50 ,default="")
    description=models.CharField(max_length=200)
    pub_date=models.DateField()
    price=models.IntegerField(default=1000)
    image=models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Complain(models.Model):
    complain_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50 ,default="")
    description=models.CharField(max_length=200)
    mobile=models.IntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=3000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=50)
    phone=models.CharField(max_length=50,default="")
    amount=models.IntegerField(default=0)

class OrderUpdate(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default="")
    update_desc=models.CharField(max_length=300)
    timestamp=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc+"..."