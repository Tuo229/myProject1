from django.db import models
from django.conf import settings

from django.contrib.auth import get_user_model

from .ville import VILLE_CHOICES, OFFRE_CHOICES, TYPE_CHOICES, NATURE_CHOICES

User = get_user_model()


class Immobilier(models.Model):
    
    #type_immob = models.ForeignKey("Types", verbose_name="Type de bien", on_delete=models.CASCADE)
    #nombre = models.IntegerField("Nombre de pièces", default=0)
    surface = models.IntegerField("Surface en m²")
    commune = models.CharField("Ville ou commune", max_length=128, choices=VILLE_CHOICES)
    prix = models.IntegerField("Prix de loyer souhaité")
    adresse = models.CharField("Adresse postale", max_length=254)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    image_1 = models.ImageField(upload_to=settings.MEDIA_ROOT)
    image_2 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    desc = models.TextField("Description du bien")
    offre = models.CharField("Offre", max_length=50, choices=OFFRE_CHOICES)
    user = models.ForeignKey(User, verbose_name="Propriétaire", on_delete=models.CASCADE)
    created_at = models.DateTimeField("Date de création", auto_now_add=True)
   
    def __str__(self):
        return self.commune

class Maison(Immobilier):
    
    types = models.CharField("Type de maison", max_length=50, choices=TYPE_CHOICES)
    nombre = models.IntegerField("Nombre de pièces")
    nb_wc = models.IntegerField("Nombre de salle d'eau")

    class Meta:
        verbose_name = "Maison"
    def __str__(self):
        return self.types

class Immeuble(Immobilier):
    
    nombre = models.IntegerField("Nombre d'étage")
    
    class Meta:
        verbose_name = "Immeuble"

    def __str__(self):
        return self.nombre


class Terrain(Immobilier): 

    nature = models.CharField("Nature foncier du terrain", max_length=50, choices=NATURE_CHOICES)
    
    class Meta:
        verbose_name = "Terrain"
    
    def __str__(self):
        return self.nature

