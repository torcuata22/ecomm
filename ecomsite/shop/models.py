from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=300)

    def __str__(self):
        return self.title

class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    zipcode=models.CharField(max_length=250)

    #def __str__(self):
        #return self.id
