from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.mongo_inventory.models import *


def mongo_list(request):
    template_name = "mongo/mongo_table.html"
    mongo_inventory = MongoInventory.objects.all()
    mongo_consumed = MongoConsumed.objects.all()
    date = datetime.date.today()
    
    try:
        total_avail_volume = MongoInventory.objects.all().order_by("-id")[0]
        print(total_avail_volume)
        total = total_avail_volume.total_avail_volume
    except:
        total = 0
    
    
    context = {
        "mongo": mongo_inventory,
        "total": total,
        "date": date
    }
    return render(request, template_name, context)
