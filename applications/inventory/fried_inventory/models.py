from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel

class FriedInventory(BaseModel):
    batch_no = models.CharField("FPID", max_length=255)
    date_fried = models.DateField("Date Fried/Packed")
    no_of_packs_30g = models.IntegerField("No. of Packs (30g)", null=True, blank=True)
    no_of_packs_15g = models.IntegerField("No. of Packs (15g)", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Fried Inventories"
        verbose_name = "Fried Inventories"

    def __str__(self):
        return f"{self.batch_no}" + " | " + f"{ self.date_fried}"