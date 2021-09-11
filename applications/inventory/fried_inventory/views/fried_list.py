from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.db.models import Sum
import datetime
from applications.inventory.fried_inventory.models import *

@login_required(login_url='/app/v1/accounts/login/')
def fried_list(request):
    template_name = "fried/fried_table.html"
    fried_inventory = FriedInventory.objects.all()
    date = datetime.date.today()
    
    
    context = {
        "fried": fried_inventory,
        "date": date
    }
    return render(request, template_name, context)
