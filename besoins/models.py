from django.db import models
from django.contrib.auth import get_user_model

from immobilier.ville import VILLE_CHOICES, OFFRE_CHOICES, TYPE_CHOICES, NATURE_CHOICES


User = get_user_model()

class Besoins(models.Model):
    
    type_bien       = models.CharField("Type de bien", max_length=50, choices=TYPE_CHOICES)
    nombre          = models.IntegerField("Nombre de pièces", blank=True, default=1)
    surface         = models.IntegerField("Superficie en m²")
    prix            = models.IntegerField("Prix minimum")
    prix_2          = models.IntegerField("Prix maximum")
    demande         = models.CharField("Demande", max_length=50, choices=OFFRE_CHOICES)
    commune         = models.CharField("Ville ou commune", max_length=128, choices=VILLE_CHOICES)
    adresse         = models.CharField("Adresse", max_length=254, blank=True, null=True)
    user            = models.ForeignKey(User, verbose_name="Demandeur", related_name="owner", on_delete=models.CASCADE)
    satisfait       = models.BooleanField(default=True)
    created_at      = models.DateTimeField("Date de création", auto_now_add=True)

    def __str__(self):
        return self.type_bien
