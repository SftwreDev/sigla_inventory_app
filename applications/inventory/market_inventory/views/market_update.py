from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.market_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_market_inventory(request):

    if request.method == 'POST':
        try:
            id = request.POST['market_id']
            cust_name = request.POST['update_cust_name']
            # lot_code = request.POST['update_lot_code']
            date_delivered = request.POST['update_date_delivered']
            extrudate = request.POST['update_batch_no_extrudate']
            fried = request.POST['update_batch_no_fried']
            lot_code = extrudate + fried

            update_object = MarketInventory.objects.filter(id=id).update(
                cust_name=cust_name,
                lot_code=lot_code,
                date_delivered=date_delivered
            )

            return redirect("market:market_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
    return redirect('dashboard:dashboard')