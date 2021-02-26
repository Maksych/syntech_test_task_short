from rest_framework.viewsets import (
    GenericViewSet, ReadOnlyModelViewSet
)
from rest_framework.mixins import CreateModelMixin

from apps.reservations.filters import TableFilter
from apps.reservations.models import Table, Reservation
from apps.reservations.serializers import (
    TableSerializer, ReservationSerializer
)
from apps.reservations.tasks import task_send_mail


class TableViewSet(ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filterset_class = TableFilter


class ReservationViewSet(CreateModelMixin, GenericViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer: ReservationSerializer) -> None:
        super().perform_create(serializer)
        reservation = serializer.instance
        task_send_mail.delay(
            reservation.id,
            reservation.table.number,
            reservation.date,
            reservation.email,
        )
