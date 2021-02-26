from django.utils.translation import gettext_lazy as _
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueTogetherValidator

from apps.reservations.models import Table, Reservation


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Reservation.objects.all(),
                fields=['table', 'date'],
                message=_('Table already reserved'),
            ),
        ]
