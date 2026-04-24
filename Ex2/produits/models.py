from django.db import models

# Create your models here.

from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    date_expiration = models.DateField()

    def __str__(self):
        return self.nom