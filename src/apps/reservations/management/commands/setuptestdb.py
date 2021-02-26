import random

from django.core.management import BaseCommand

from apps.reservations.models import Figure, Table


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Table.objects.all().exists():
            Table.objects.bulk_create([
                Table(
                    number=number,
                    figure=random.choice(Figure.values),
                    coord_x=number * number,
                    coord_y=number * number,
                    width=5,
                    height=5,
                )
                for number in range(10)
            ])
