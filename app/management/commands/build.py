import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "build frontend"

    def handle(self, *args, **options):
        subprocess.run(["pnpm", "build"], cwd="frontend")
