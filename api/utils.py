from django.db import models


class AbstractTableMeta(models.Model):
    """
    Table meta data which will be used by all the tables in the system
    """
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True
