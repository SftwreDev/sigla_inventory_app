from django.shortcuts import render, redirect
from django.db.models.functions import ExtractWeek, ExtractYear
from applications.inventory.mongo_inventory.views.mongo_list import *
from applications.inventory.mongo_inventory.models import *
from applications.inventory.rice_inventory.models import *
from applications.inventory.sesame_inventory.models import *
from applications.inventory.extrudate_inventory.models import *
from applications.inventory.flavourings_inventory.models import *
from applications.inventory.fried_inventory.models import *
from applications.inventory.market_inventory.models import *

def dashboard_page(request):
    """
        Function for creating dashboard page
    """
    template_name = "dashboard/dashboard.html"
    mongo = MongoInventory.objects.aggregate(Sum("total_avail_volume"))
    rice = RiceInventory.objects.aggregate(Sum("total_avail_volume"))
    sesame = SesameInventory.objects.aggregate(Sum("total_avail_volume"))
    extrudate = ExtruDateInventory.objects.aggregate(Sum("total_volume"))
    flavourings = FlavouringsInventory.objects.aggregate(Sum("total_avail_volume"))
    fried_15g = FriedInventory.objects.values_list("no_of_packs_15g", flat=True).aggregate(Sum("no_of_packs_15g"))
    fried_30g = FriedInventory.objects.values_list("no_of_packs_30g", flat=True).aggregate(Sum("no_of_packs_30g"))
    market_total = MarketInventory.objects.all().count()


    mongo_total = mongo["total_avail_volume__sum"]
    rice_total = rice["total_avail_volume__sum"]
    sesame_total = sesame["total_avail_volume__sum"]
    extrudate_total = extrudate["total_volume__sum"]
    flavourings_total = flavourings["total_avail_volume__sum"]
    fried_15g_total = fried_15g["no_of_packs_15g__sum"]
    fried_30g_total = fried_30g["no_of_packs_30g__sum"]


    context = {
        "mongo_total" : mongo_total,
        "rice_total" : rice_total,
        "sesame_total" : sesame_total,
        "extrudate_total" : extrudate_total,
        "flavourings_total" : flavourings_total,
        "fried_15g_total" : fried_15g_total,
        "fried_30g_total" : fried_30g_total,
        "market_total" : market_total
    }
    return render(request, template_name, context)


def inventory_menu(request):
    template_name = "menu/dashboard_menu.html"

    return render(request, template_name)