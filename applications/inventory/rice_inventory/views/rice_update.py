from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.rice_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_rice_inventory(request):

    if request.method == 'POST':
        try:
            if request.method == 'POST':
                rice_id = request.POST['rice_id']
                id = request.POST['inventory_id']
                batch_no = request.POST['update_batch_no']
                date_received = request.POST['update_date_received']
                date_consumed = request.POST['update_date_consumed']
                amount_consumed = request.POST['update_amount_consumed']
                parse_date = parse(date_received)
                received_date = datetime.datetime.strftime(parse_date, '%Y-%m-%d')
                

                total_avail_volume = RiceInventory.objects.all().order_by("-id")[0]
                volume_left = total_avail_volume.total_avail_volume
                latest_vol = volume_left - int(amount_consumed)
                
                update_object = RiceConsumed.objects.filter(inventory_id=rice_id).create(
                    rice_id=generate_id(),
                    inventory_id_id=rice_id,
                    date_consumed=date_consumed,
                    amount_consumed=amount_consumed,
                    total_avail_volume=volume_left
                )

                if latest_vol != 0:
                    update_inventory = RiceInventory.objects.filter(rice_id=id).update(
                        total_avail_volume=0
                    )
                    create_object = RiceInventory.objects.create(
                        rice_id=generate_id(),
                        batch_no=batch_no,
                        date_received=received_date,
                        total_avail_volume=latest_vol
                    )
                else:
                    update_inventory = RiceInventory.objects.filter(rice_id=id).update(
                        total_avail_volume=0
                    )
   
                return redirect("rice:rice_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
    return redirect('dashboard:dashboard')
