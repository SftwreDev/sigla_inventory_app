from django.urls import path

from applications.inventory.market_inventory.views.market_list import *
from applications.inventory.market_inventory.views.market_create import *
from applications.inventory.market_inventory.views.market_update import *

app_name = "market"

urlpatterns = [
    path("market-inventory/", market_list, name="market_list"),
    path("add-market", add_market_inventory, name="add_market"),
    path("update-market", update_market_inventory, name="update_mongo")
]
