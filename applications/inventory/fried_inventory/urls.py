from django.urls import path

from applications.inventory.fried_inventory.views.fried_list import *
from applications.inventory.fried_inventory.views.fried_create import *
from applications.inventory.fried_inventory.views.fried_update import *

app_name = "fried"

urlpatterns = [
    path("fried-packed-inventory/", fried_list, name="fried_list"),
    path("add-fried-packed", add_fried_packed_inventory, name="add_extrudate"),
    path("update-fried-packed", update_fried_packed_inventory, name="update_mongo")
]
