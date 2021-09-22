from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
import datetime
from applications.inventory.extrudate_inventory.models import *
from applications.inventory.mongo_inventory.models import *
from applications.inventory.rice_inventory.models import *
from applications.inventory.sesame_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def extrudate_list(request):
    template_name = "extrudate/extrudate_table.html"
    extrudate_inventory = ExtruDateInventory.objects.all()
    date = datetime.date.today()
    
    mongo = MongoInventory.objects.values_list('batch_no', flat=True).distinct()
    rice = RiceInventory.objects.values_list('batch_no', flat=True).distinct()
    sesame = SesameInventory.objects.values_list('batch_no', flat=True).distinct()
    
    context = {
        "extrudate": extrudate_inventory,
        "date": date,
        "mongo" : mongo,
        "rice" : rice,
        "sesame" : sesame,
    }
    return render(request, template_name, context)
