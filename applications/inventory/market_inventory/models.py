from django.db import models

# Create your models here.
from applications.base_settings.models import BaseModel
from applications.base_settings.uuid_generator import *


class MarketInventory(BaseModel):
    market_id = models.CharField("Market ID",max_length=255, default=generate_id(), editable=False )
    cust_name = models.CharField("Customer Name",max_length=2255)
    lot_code = models.CharField("Lot Code", max_length=255)
    date_delivered = models.DateField("Date Delivered", auto_now_add=False)

    class Meta:
        verbose_name_plural = "Market Inventories"
        verbose_name = "Market Inventories"
        db_table = "market_inventory"

    def __str__(self):
        return f"{self.cust_name}" + " | " + f"{self.lot_code}" + " | " + f"{self.date_delivered}"
