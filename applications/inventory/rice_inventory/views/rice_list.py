from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.rice_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def rice_list(request):
    template_name = "rice/rice_table.html"
    rice_inventory = RiceInventory.objects.all()
    rice_consumed = RiceConsumed.objects.all()
    date = datetime.date.today()
    total_avail_volume = RiceInventory.objects.aggregate(Sum('total_avail_volume'))
    total = total_avail_volume["total_avail_volume__sum"]
    if total != None:
        total = total
    else:
        total = 0
    
    
    context = {
        "rice": rice_inventory,
        "total": total,
        "date": date
    }
    return render(request, template_name, context)
