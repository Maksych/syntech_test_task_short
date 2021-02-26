from django_filters import rest_framework as filters

from apps.reservations.models import Table


class TableFilter(filters.FilterSet):
    date = filters.DateFilter(
        field_name='reservation__date',
        exclude=True,
        required=True,
    )

    class Meta:
        model = Table
        fields = ['date']
