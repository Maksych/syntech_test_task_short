import datetime

from unittest.mock import patch

from django.test import TestCase

from rest_framework.test import APIClient

from apps.reservations.models import Figure, Table
from apps.reservations.tasks import task_send_mail


@patch('apps.reservations.tasks.task_send_mail.delay', task_send_mail)
class ReservationTestCase(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

        self.date = datetime.date.today().isoformat()

        Table.objects.bulk_create([
            Table(
                number=number,
                figure=Figure.SQUARE,
                coord_x=1,
                coord_y=1,
                width=1,
                height=1,
            )
            for number in range(10)
        ])

    def test_tables_date_not_exists(self):
        response = self.client.get('/api/v1/tables/')

        # NOTE: query param 'date' is missing -> Bad Request 400
        self.assertEqual(response.status_code, 400)

    def test_tables_date_exists(self):
        response = self.client.get(
            '/api/v1/tables/',
            data={'date': self.date},
        )

        # NOTE: successful response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 10)

    def test_reservation_successful(self):
        response = self.reserve()

        # NOTE: successful response
        self.assertEqual(response.status_code, 201)

    def reserve(
            self,
            table_id: int = 1,
            date: str = None,
            email: str = 'example@email.com'
    ):
        return self.client.post(
            '/api/v1/reservations/',
            data={
                'table': table_id,
                'date': date or self.date,
                'email': email,
            },
        )

    def test_reservation_already_reserved(self):
        self.reserve()
        response = self.reserve()

        # NOTE: check reserved table
        self.assertEqual(response.status_code, 400)
