import datetime

from celery import shared_task
from django.core.mail import send_mail


@shared_task
def task_send_mail(
        reservation_id: int,
        table_number: int,
        date: datetime.date,
        email: str,
) -> None:
    send_mail(
        f'Reservation #{reservation_id}',
        (
            f'Date {date}'
            f'Reserved table #{table_number}'
        ),
        'from@example.com',
        [email],
    )
