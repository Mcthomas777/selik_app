from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import json

from .models import Property, ChangeLog

@receiver(post_save, sender=Property)
def log_property_save(sender, instance, created, **kwargs):
    action = "Création" if created else "Modification"
    ChangeLog.objects.create(object_type='bien', object_id=instance.id, action=action, changes=json.dumps({
        'titre': instance.property_titre, 'adresse': instance.property_adresse
    }))