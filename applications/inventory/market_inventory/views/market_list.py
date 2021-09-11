from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.market_inventory.models import *
from applications.inventory.extrudate_inventory.models import *
from applications.inventory.fried_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def market_list(request):
    template_name = "market/market_table.html"
    market_inventory = MarketInventory.objects.all()
    date = datetime.date.today()
    
    extrudate = ExtruDateInventory.objects.values_list('batch_no', flat=True)
    fried = FriedInventory.objects.values_list('batch_no', flat=True)
    
    context = {
        "market": market_inventory,
        "date": date,
        "extrudate" : extrudate,
        "fried" : fried
    }
    return render(request, template_name, context)
