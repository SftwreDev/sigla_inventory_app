from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel

class FriedInventory(BaseModel):
    batch_no = models.IntegerField("Batch No.")
    date_fried = models.DateField("Date Fried/Packed")

    class Meta:
        verbose_name_plural = "Fried Inventories"
        verbose_name = "Fried Inventories"

    def __str__(self):
        return f"{self.batch_no}" + " | " + f"{ self.date_fried}"