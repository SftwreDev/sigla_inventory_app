from django.shortcuts import redirect, render
import datetime
from dateutil.parser import parse
from applications.inventory.mongo_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_mongo_inventory(request):

    if request.method == 'POST':
        try:
            if request.method == 'POST':
                mongo_id = request.POST['mongo_id']
                batch_no = request.POST['update_batch_no']
                new_batch_no = request.POST['new_batch_no']
                date_received = request.POST['update_date_received']
                date_consumed = request.POST['update_date_consumed']
                amount_consumed = request.POST['update_amount_consumed']
                parse_date = parse(date_received)
                received_date = datetime.datetime.strftime(parse_date, '%Y-%m-%d')

                update_object = MongoInventory.objects.filter(mongo_id=mongo_id).update(
                    date_consumed=date_consumed,
                    amount_consumed=amount_consumed
                )

                total_avail_volume = MongoInventory.objects.filter(batch_no=batch_no)
                for volume in total_avail_volume:
                    volume_left = volume.total_avail_volume
                volume_left = volume_left
                latest_vol = volume_left - int(amount_consumed)
                
                create_object = MongoInventory.objects.create(
                    mongo_id=generate_id(),
                    batch_no=new_batch_no,
                    date_received=received_date,
                    total_avail_volume=latest_vol
                )

                return redirect("mongo:mongo_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
    return redirect('dashboard:dashboard')
