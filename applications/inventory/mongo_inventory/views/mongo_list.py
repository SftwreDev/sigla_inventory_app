from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.mongo_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def mongo_list(request):
    template_name = "mongo/mongo_table.html"
    mongo_inventory = MongoInventory.objects.all()
    mongo_consumed = MongoConsumed.objects.all()
    date = datetime.date.today()
    total_avail_volume = MongoInventory.objects.aggregate(Sum('total_avail_volume'))
    total = total_avail_volume["total_avail_volume__sum"]
    if total != None:
        total = total
    else:
        total = 0
    
    
    context = {
        "mongo": mongo_inventory,
        "total": total,
        "date": date
    }
    return render(request, template_name, context)
