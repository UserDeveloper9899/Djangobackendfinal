from django.db import models
import datetime

# Create your models here.
class Item(models.Model):
    companyname=models.CharField(max_length=50, unique=True)
    code=models.IntegerField(unique=True)
    ceo=models.CharField(max_length=20)
    turnover=models.IntegerField()
    website=models.CharField(max_length=50)
    stockenlist=models.CharField(max_length=3)

    def __str__(self):
        return self.companyname
class Price(models.Model):
    companyname=models.ForeignKey(Item,on_delete=models.CASCADE, related_name='prices')
    #sdate=models.DateTimeField(auto_now_add=True,null=True)
    price_stock=models.DecimalField(default=0.00,max_digits=10,decimal_places=3)
    created=models.DateField(default=datetime.date.today)                                     #DateField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.price_stock)

