from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def asignar_rol(sender, instance, created, **kwargs):
    if created:
        grupo, _ = Group.objects.get_or_create(name="Usuario")
        instance.groups.add(grupo)