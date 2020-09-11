from django.db import models


class AbstractTableMeta(models.Model):
    """
    Table meta data which will be used by all the tables in the system
    """
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class Vehicle(AbstractTableMeta, models.Model):
    registration_no = models.CharField(max_length=40, default='', blank='True')

    class Meta:
        db_table = "vehicle"


class Slot(AbstractTableMeta, models.Model):
    slot_no = models.IntegerField(unique=True)
    parked_vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = "slot"
