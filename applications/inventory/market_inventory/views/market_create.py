from django.shortcuts import redirect, render

from applications.inventory.market_inventory.models import *


def add_market_inventory(request):

    if request.method == 'POST':
        try:
            template = "dashboard/mongo/mongo_js.html"
            cust_name = request.POST['cust_name']
            # lot_code = request.POST['lot_code']
            extrudate = request.POST['batch_no_extrudate']
            fried = request.POST['batch_no_fried']
            date_delivered = request.POST['date_delivered']
            lot_code = extrudate + fried

            create_object = MarketInventory.objects.create(
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
