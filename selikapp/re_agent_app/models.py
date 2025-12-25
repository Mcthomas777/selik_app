from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

from .constants import PROPERTY_TYPE_CHOICES, PROPERTY_STATUS_CHOICES

User = get_user_model()

class Contact(models.Model):
    contact_type = models.CharField(max_length=50, choices=[('acquéreur', 'Acquéreur'), ('locataire', 'Locataire'), ('propriétaire', 'Propriétaire'), ('notaire', 'Notaire'), ("syndic", "Syndic")], default='acheteur')
    contact_first_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=200)
    contact_nego = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    contact_email = models.EmailField(blank=True, null=True)
    contact_telephone = models.CharField(max_length=50, blank=True)
    contact_status = models.CharField(max_length=50, choices=[('actif', 'Actif'), ('archivé', 'Archivé')], default='actif')
    contact_adress = models.CharField(max_length=255, blank=True)
    contact_complement_adress = models.CharField(max_length=255, blank=True)

    # Contact additionnal Information
    contact_commentar = models.TextField(blank=True)
    contact_created_at = models.DateTimeField(auto_now_add=True)

    # Criteria
    contact_cr_type_search = models.CharField(max_length=50, choices=[('vente', 'Vente'), ('location', 'Location')], default='vente')
    contact_cr_type_estatse = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES, default='appartement')
    contact_cr_budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    contact_cr_room_number = models.IntegerField(blank=True, null=True)
    contact_cr_bedroom_number = models.IntegerField(blank=True, null=True)
    contact_cr_surface = models.FloatField(blank=True, null=True)
    contact_cr_surface_terrain = models.FloatField(blank=True, null=True)


class Mandat(models.Model):
    reference = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date_start = models.DateField(default=timezone.now)
    client = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Property(models.Model):
    # Information générales
    property_type_tansaction = models.CharField(max_length=50, choices=[('vente', 'Vente'), ('location', 'Location')], default='vente')
    property_type = models.CharField(max_length=100, choices=PROPERTY_TYPE_CHOICES, default='appartement')
    property_info_complémentaire = models.CharField(max_length=50, blank=True, null=True, choices=[('VEFA', 'VEFA'), ('occupé', 'Occupé'), ('villa', 'Villa'), ('chalet_bois', 'Chalet en bois')])
    property_surface = models.FloatField()
    property_surface_terrain = models.FloatField(blank=True, null=True)
    property_négociateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    property_status = models.CharField(max_length=50, choices=PROPERTY_STATUS_CHOICES, default='disponible')
    property_titre = models.CharField(max_length=255)
    property_numéro_clé = models.CharField(max_length=100, blank=True, null=True)
    property_diffusé = models.BooleanField(default=False)
    property_description = models.TextField(blank=True)
    property_created_at = models.DateTimeField(auto_now_add=True)

    # Informations Financières
    property_prix_hors_honoraires = models.DecimalField(max_digits=12, decimal_places=2)
    property_honoraires = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    property_taux_commision = models.FloatField(blank=True, null=True, default=4.5)
    property_prix = models.DecimalField(max_digits=12, decimal_places=2)
    property_charge_honoraire = models.CharField(max_length=50, choices=[('vendeur', 'Vendeur'), ('acquéreur', "Acquéreur")], default='acquéreur')
    property_taxe_foncière = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    property_taxe_habitation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    property_charge_mensuelle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    #Contact & Localisation
    property_contacts = models.ManyToManyField(Contact, blank=True)
    property_adresse = models.CharField(max_length=255)
    property_complement_adresse = models.CharField(max_length=255, blank=True)


class BienImage(models.Model):
    property_parent = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="images")
    property_image = models.ImageField(upload_to="biens/")
    property_image_vitrine = models.BooleanField(default=False)


class Visite(models.Model):
    bien = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='visites')
    date = models.DateTimeField()
    visiteur = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ActionCommerciale(models.Model):
    titre = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    bien = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ChangeLog(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('bien', 'Bien'),
        ('mandat', 'Mandat'),
        ('contact', 'Contact'),
        ('visite', 'Visite'),
        ('action', 'ActionCommerciale'),
    ]
    object_type = models.CharField(max_length=30, choices=CONTENT_TYPE_CHOICES)
    object_id = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    action = models.CharField(max_length=100)  # ex: "Création", "Modification", "Suppression"
    changes = models.TextField(blank=True)      # JSON or human-readable
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']


class Negociator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    agency = models.CharField(max_length=255, blank=True, null=True)
    agency_address = models.CharField(max_length=255, blank=True, null=True)
    agency_phone = models.CharField(max_length=20, blank=True, null=True)
    agency_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() 

class City(models.Model):
    name = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.postal_code})"
