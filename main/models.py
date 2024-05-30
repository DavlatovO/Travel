from django.db import models

class Carrier(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Hotel(models.Model):
    name = models.CharField(max_length=255)
    stars = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)



class Travel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    carrier = models.ForeignKey(Carrier, on_delete=models.CASCADE) 
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)





    