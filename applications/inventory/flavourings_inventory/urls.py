from django.urls import path

from applications.inventory.flavourings_inventory.views.flavourings_list import *
from applications.inventory.flavourings_inventory.views.flavourings_create import *
from applications.inventory.flavourings_inventory.views.flavourings_update import *

app_name = "flavourings"

urlpatterns = [
    path("flavourings-inventory/", flavourings_list, name="flavourings_list"),
    path("add-flavourings", add_flavourings_inventory, name="add_flavourings"),
    path("update-flavourings", update_flavourings_inventory, name="update_mongo")
]
