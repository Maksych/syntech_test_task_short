from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _


class Figure(models.TextChoices):
    CIRCLE = 'CIRCLE', _('Circle')
    ELLIPSE = 'ELLIPSE', _('Ellipse')
    RECTANGLE = 'RECTANGLE', _('Rectangle')
    SQUARE = 'SQUARE', _('Square')


class Table(models.Model):
    number = models.PositiveIntegerField(
        _('Number'),
        default=1,
        unique=True,
        validators=[MinValueValidator(1)],
    )
    seats = models.PositiveIntegerField(
        _('Seats'),
        default=1,
        validators=[MinValueValidator(1)],
    )
    figure = models.CharField(
        _('Figure'),
        max_length=31,
        choices=Figure.choices,
    )

    # coords
    coord_x = models.PositiveIntegerField(
        _('X Coord (in percents)'),
    )
    coord_y = models.PositiveIntegerField(
        _('Y Coord (in percents)'),
    )

    # size
    width = models.PositiveIntegerField(
        _('Width (in percents)'),
    )
    height = models.PositiveIntegerField(
        _('Height (in percents)'),
    )


class Reservation(models.Model):
    table = models.ForeignKey(
        Table,
        on_delete=models.CASCADE,
        verbose_name=_('Table'),
    )

    date = models.DateField()
    email = models.EmailField()

    class Meta:
        unique_together = ['table', 'date']
