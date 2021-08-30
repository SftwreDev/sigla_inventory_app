from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel
from applications.base_settings.uuid_generator import *


class MongoInventory(BaseModel):
    mongo_id = models.CharField("ID", max_length=255, default=generate_id())
    batch_no = models.CharField("Batch No.", max_length=255)
    date_received = models.DateField("Date Received",auto_now_add=False)
    total_avail_volume = models.IntegerField("Total Available Volume")
    amount_consumed = models.IntegerField("Amount Consumed", blank=True, null=True)
    date_consumed = models.DateField("Date Consumed",auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = "Mongo Inventory"
        verbose_name_plural = "Mongo Inventories"
    
    def __str__(self):
        return "Batch No. : " +  f"{ self.batch_no }" + " | " + f"{ self.date_received }"