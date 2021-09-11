from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.flavourings_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def flavourings_list(request):
    template_name = "flavourings/flavourings_table.html"
    flavourings_inventory = FlavouringsInventory.objects.all()
    date = datetime.date.today()
    total_avail_volume = FlavouringsInventory.objects.aggregate(Sum('total_avail_volume'))
    total = total_avail_volume["total_avail_volume__sum"]
    if total != None:
        total = total
    else:
        total = 0
    
    
    context = {
        "flavourings": flavourings_inventory,
        "date": date,
        "total" : total
    }
    return render(request, template_name, context)
