from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.flavourings_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_flavourings_inventory(request):

     if request.method == 'POST':
        try:
            if request.method == 'POST':
                flavourings_id = request.POST['flavourings_id']
                id = request.POST['inventory_id']
                batch_no = request.POST['update_batch_no']
                date_received = request.POST['update_date_received']
                flavourings = request.POST['update_flavourings']
                date_consumed = request.POST['update_date_consumed']
                amount_consumed = request.POST['update_amount_consumed']
                total_volume = request.POST['update_total_avail_volume']
                parse_date = parse(date_received)
                received_date = datetime.datetime.strftime(parse_date, '%Y-%m-%d')
                

                total_avail_volume = FlavouringsInventory.objects.all().order_by("-id")[0]
                volume_left = total_avail_volume.total_avail_volume
                latest_vol = int(total_volume) - int(amount_consumed)
                
                update_object = FlavouringsConsumed.objects.filter(inventory_id=flavourings_id).create(
                    flavourings_id=generate_id(),
                    inventory_id_id=flavourings_id,
                    date_consumed=date_consumed,
                    amount_consumed=amount_consumed,
                    total_avail_volume= int(total_volume),
                )

                if latest_vol != 0:
                    update_inventory = FlavouringsInventory.objects.filter(id=flavourings_id).update(
                        total_avail_volume=0
                    )
                    create_object = FlavouringsInventory.objects.create(
                        flavourings_id=generate_id(),
                        batch_no=batch_no,
                        date_received=received_date,
                        total_avail_volume=latest_vol,
                        flavourings=flavourings
                    )
                else:
                    update_inventory = FlavouringsInventory.objects.filter(id=flavourings_id).update(
                        total_avail_volume=0
                    )
   
                return redirect("flavourings:flavourings_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
        return redirect('dashboard:dashboard')
