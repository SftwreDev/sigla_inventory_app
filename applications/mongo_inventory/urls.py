from django.urls import path

from applications.mongo_inventory.views.mongo_create import *
from applications.mongo_inventory.views.mongo_list import *
from applications.mongo_inventory.views.mongo_update import *

app_name = "mongo"

urlpatterns = [
    path("mongo-inventory/", mongo_list, name="mongo_list"),
    path("add-mongo", add_mongo_inventory, name="add_mongo"),
    path("update-mongo", update_mongo_inventory, name="update_mongo")
]
