from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits = 5,decimal_places = 2)
    def __str__(self):
        return self.id