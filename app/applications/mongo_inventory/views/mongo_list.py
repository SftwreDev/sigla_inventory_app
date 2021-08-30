from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.mongo_inventory.models import *


def mongo_list(request):
    template_name = "mongo/mongo_table.html"
    batch_mongo = MongoInventory.objects.all()
    date = datetime.date.today()
    total_avail_volume = MongoInventory.objects.filter(amount_consumed=None, date_consumed=None)
    
    for total_avail in total_avail_volume:
        total = total_avail.total_avail_volume

    total=total

    
    context = {
        "mongo": batch_mongo,
        "total": total,
        "date": date
    }
    return render(request, template_name, context)
