from django.urls import path

from applications.inventory.sesame_inventory.views.sesame_list import *
from applications.inventory.sesame_inventory.views.sesame_create import *
from applications.inventory.sesame_inventory.views.sesame_update import *

app_name = "sesame"

urlpatterns = [
    path("sesame-inventory/", sesame_list, name="sesame_list"),
    path("add-sesame", add_sesame_inventory, name="add_sesame"),
    path("update-sesame", update_sesame_inventory, name="update_sesame")
]
