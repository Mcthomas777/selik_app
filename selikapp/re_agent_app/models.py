from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

ESTATE_TYPE = (
    ('appartement', 'Appartement'),
    ('maison', 'Maison'),
    ('terrain', 'Terrain'),
    ('local_commercial', 'Local Commercial'),
    ('garage', 'Garage'),
    ('parking', 'Parking'),
    ('immeuble', 'Immeuble'),
    ('fond_de_commerce', 'Fond de Commerce'),
    ('ensemble_immobilier', 'Ensemble Immobilier'),
)

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
    contact_cr_type_estatse = models.CharField(max_length=100, choices=ESTATE_TYPE, default='appartement')
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


class Bien(models.Model):
    # Information générales
    bien_type_tansaction = models.CharField(max_length=50, choices=[('vente', 'Vente'), ('location', 'Location')], default='vente')
    bien_type = models.CharField(max_length=100, choices=ESTATE_TYPE, default='appartement')
    bien_info_complémentaire = models.CharField(max_length=50, blank=True, null=True, choices=[('VEFA', 'VEFA'), ('occupé', 'Occupé'), ('villa', 'Villa'), ('chalet_bois', 'Chalet en bois')])
    bien_surface = models.FloatField()
    bien_surface_terrain = models.FloatField(blank=True, null=True)
    bien_négociateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bien_status = models.CharField(max_length=50, choices=[('actif', 'Actif'), ('estimation', 'Estimation'), ('archivé', 'Archivé')], default='disponible')
    bien_titre = models.CharField(max_length=255)
    bien_numéro_clé = models.CharField(max_length=100, blank=True, null=True)
    bien_diffusé = models.BooleanField(default=False)
    bien_description = models.TextField(blank=True)
    bien_created_at = models.DateTimeField(auto_now_add=True)

    # Informations Financières
    bien_prix_hors_honoraires = models.DecimalField(max_digits=12, decimal_places=2)
    bien_honoraires = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    bien_taux_commision = models.FloatField(blank=True, null=True, default=4.5)
    bien_prix = models.DecimalField(max_digits=12, decimal_places=2)
    bien_charge_honoraire = models.CharField(max_length=50, choices=[('vendeur', 'Vendeur'), ('acquéreur', "Acquéreur")], default='acquéreur')
    bien_taxe_foncière = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bien_taxe_habitation = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    bien_charge_mensuelle = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    #Contact & Localisation
    bien_contacts = models.ManyToManyField(Contact, blank=True)
    bien_adresse = models.CharField(max_length=255)
    bien_complement_adresse = models.CharField(max_length=255, blank=True)

class Visite(models.Model):
    bien = models.ForeignKey(Bien, on_delete=models.CASCADE, related_name='visites')
    date = models.DateTimeField()
    visiteur = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ActionCommerciale(models.Model):
    titre = models.CharField(max_length=255)
    detail = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    bien = models.ForeignKey(Bien, on_delete=models.SET_NULL, null=True, blank=True)
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

