from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.extrudate_inventory.models import *


def extrudate_list(request):
    template_name = "extrudate/extrudate_table.html"
    extrudate_inventory = ExtruDateInventory.objects.all()
    date = datetime.date.today()
    
    
    context = {
        "mongo": extrudate_inventory,
        "date": date
    }
    return render(request, template_name, context)
