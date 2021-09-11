from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.sesame_inventory.models import *


@login_required(login_url='/app/v1/accounts/login/')
def sesame_list(request):
    template_name = "sesame/sesame_table.html"
    sesame_inventory = SesameInventory.objects.all()
    sesame_consumed = SesameConsumed.objects.all()
    date = datetime.date.today()
    total_avail_volume = SesameInventory.objects.aggregate(Sum('total_avail_volume'))
    total = total_avail_volume["total_avail_volume__sum"]
    if total != None:
        total = total
    else:
        total = 0
    
    
    context = {
        "sesame": sesame_inventory,
        "total": total,
        "date": date
    }
    return render(request, template_name, context)
