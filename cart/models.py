from django.db import models

class Suit(models.Model):
    suit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    availability_status = models.BooleanField(default=True)  # True means available for rent/buy

    def __str__(self):
        return self.name
