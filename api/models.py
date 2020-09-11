from django.db import models

# Create your models here.
from api.utils import AbstractTableMeta


class Vehicle(AbstractTableMeta, models.Model):
    registration_no = models.CharField(max_length=40, default='', blank='True')

    class Meta:
        db_table = "vehicle"


class Slot(AbstractTableMeta, models.Model):
    slot_no = models.IntegerField()
    parked_vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "slot"
