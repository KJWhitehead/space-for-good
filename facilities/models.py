from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


class Facilities(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Space(models.Model):

    TYPES = (
        ("Meeting Room", "Meeting Room"),
        ("Open Seating", "Open Seating"),
    )

    name = models.CharField(max_length=50, null=False, blank=False)
    max_capacity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(12)],
        null=False, blank=False
    )
    space_type = models.CharField(
        choices=TYPES, max_length=20, null=False, blank=False
    )

    def __str__(self):
        return self.name


class Reservation(models.Model):

    TIMES = (
        ("09:00-11:00", "09:00-11:00"),
        ("11:00-13:00", "11:00-13:00"),
        ("13:00-15:00", "13:00-15:00"),
        ("15:00-17:00", "15:00-17:00"),
        ("17:00-19:00", "17:00-19:00"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="main.Reservation.user+"
    )
    space = models.ForeignKey(
        Space, on_delete=models.CASCADE,
        related_name="main.Reservation.space+"
    )
    date = models.DateField(null=False, blank=False)
    time = models.CharField(
        choices=TIMES, max_length=20, null=False, blank=False
    )

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.space} on {self.date} {self.time}"