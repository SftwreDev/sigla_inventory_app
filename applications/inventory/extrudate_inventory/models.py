from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel
from applications.base_settings.uuid_generator import *


class ExtruDateInventory(BaseModel):
    extru_id = models.CharField("ID", max_length=255, default=generate_id(), editable=False)
    batch_no = models.CharField("EXTID", max_length=255)
    date_produced = models.DateField("Date Produced",auto_now_add=False)
    total_volume = models.IntegerField("Total Volume (kg.)")
    mongo_batch_no = models.CharField("Batch No. of Mongo", max_length=255)
    rice_batch_no = models.CharField("Batch No. of Rice", max_length=255)
    sesame_batch_no = models.CharField("Batch No. of Sesame", max_length=255)

    class Meta:
        verbose_name = "ExtruDates"
        verbose_name_plural = "ExtruDates"
        db_table = "extrudate_inventory"

    def __str__(self):
        return f"{self.batch_no}"