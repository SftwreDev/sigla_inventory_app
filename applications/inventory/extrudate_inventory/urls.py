from django.urls import path

# from applications.inventory.extrudate_inventory.views.mongo_create import *
from applications.inventory.extrudate_inventory.views.extrudates_list import *
# from applications.inventory.mongo_inventory.views.mongo_update import *

app_name = "extrudate"

urlpatterns = [
    path("extrudate-inventory/", extrudate_list, name="extrudate_list"),
    # path("add-mongo", add_mongo_inventory, name="add_mongo"),
    # path("update-mongo", update_mongo_inventory, name="update_mongo")
]
