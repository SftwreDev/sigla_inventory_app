from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel
from applications.base_settings.uuid_generator import *


class RiceInventory(BaseModel):
    rice_id = models.CharField("ID", max_length=255, default=generate_id(), editable=False)
    batch_no = models.CharField("RID", max_length=255)
    date_received = models.DateField("Date Received",auto_now_add=False)
    total_avail_volume = models.IntegerField("Total Available Volume")

    class Meta:
        verbose_name = "Rice Inventory"
        verbose_name_plural = "Rice Inventories"
        db_table = "rice_inventory"
    
    def __str__(self):
        return "Batch No. : " +  f"{ self.batch_no }" + " | " + f"{ self.date_received }"


class RiceConsumed(models.Model):
    rice_id = models.CharField("ID", max_length=255, default=generate_id(), editable=False)
    inventory_id = models.ForeignKey(RiceInventory, on_delete=models.CASCADE, related_name="rice_inventory")
    total_avail_volume = models.IntegerField("Total Available Volume")
    amount_consumed = models.IntegerField("Amount Consumed", blank=True, null=True)
    date_consumed = models.DateField("Date Consumed",auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = "Rice Consumed"
        verbose_name_plural = "Rice Consumed"
        db_table = "rice_consumed"
    
    def __str__(self):
        return "Batch No. : " +  f"{ self.inventory_id.batch_no }" + " | " + "Amount Consumed : " +  f"{ self.amount_consumed }"