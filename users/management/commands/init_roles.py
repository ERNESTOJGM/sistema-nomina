from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Crea los 4 roles base"
    def handle(self, *args, **options):
        for rol in ["Administrador", "Gestor", "Usuario", "Visitante"]:
            g, c = Group.objects.get_or_create(name=rol)
            self.stdout.write(self.style.SUCCESS(f"OK: {rol}") if c else f"Ya existia: {rol}")