from django.urls import path

from applications.inventory.extrudate_inventory.views.extrudates_list import *
from applications.inventory.extrudate_inventory.views.extrudates_create import *
from applications.inventory.extrudate_inventory.views.extrudates_update import *

app_name = "extrudate"

urlpatterns = [
    path("extrudate-inventory/", extrudate_list, name="extrudate_list"),
    path("add-extrudate", add_extrudate_inventory, name="add_extrudate"),
    path("update-extrudate", update_extrudate_inventory, name="update_extrudate")
]
