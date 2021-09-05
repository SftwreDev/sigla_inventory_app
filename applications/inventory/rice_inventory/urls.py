from django.urls import path

from applications.inventory.rice_inventory.views.rice_list import *
from applications.inventory.rice_inventory.views.rice_create import *
from applications.inventory.rice_inventory.views.rice_update import *

app_name = "rice"

urlpatterns = [
    path("rice-inventory/", rice_list, name="rice_list"),
    path("add-rice", add_rice_inventory, name="add_rice"),
    path("update-rice", update_rice_inventory, name="update_rice")
]
