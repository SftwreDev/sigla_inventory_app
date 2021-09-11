from applications.base_settings.uuid_generator import generate_id
from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel



class FlavouringsInventory(BaseModel):
    flavourings_id = models.CharField("ID", max_length=255, default=generate_id(), editable=False)
    batch_no = models.CharField("Batch No.", max_length=255)
    date_received = models.DateField("Date Received",auto_now_add=False)
    total_avail_volume = models.IntegerField("Total Available Volume")
    flavourings = models.CharField("Flavourings",max_length=255)

    class Meta:
        verbose_name =  "Flavourings Inventories"
        verbose_name_plural =  "Flavourings Inventories"
        db_table = "flavourings_inventory"
    
    def __str__(self):
        return "Batch No. : " +  f"{ self.batch_no }" + " | " + f"{ self.date_received }"


class FlavouringsConsumed(models.Model):
    flavourings_id = models.CharField("ID", max_length=255, default=generate_id(), editable=False)
    inventory_id = models.ForeignKey(FlavouringsInventory, on_delete=models.CASCADE, related_name="flavourings_inventory")
    total_avail_volume = models.IntegerField("Total Available Volume")
    amount_consumed = models.IntegerField("Amount Consumed", blank=True, null=True)
    date_consumed = models.DateField("Date Consumed",auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = "Flavourings Consumed"
        verbose_name_plural = "Flavourings Consumed"
        db_table = "flavourings_consumed"
    
    def __str__(self):
        return "Batch No. : " +  f"{ self.inventory_id.batch_no }" + " | " + "Amount Consumed : " +  f"{ self.amount_consumed }"