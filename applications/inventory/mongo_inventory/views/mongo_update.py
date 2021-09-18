from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.mongo_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_mongo_inventory(request):
    if request.method == 'POST':
        try:
            if request.method == 'POST':
                mongo_id = request.POST['mongo_id']
                id = request.POST['inventory_id']
                batch_no = request.POST['update_batch_no']
                date_received = request.POST['update_date_received']
                date_consumed = request.POST['update_date_consumed']
                amount_consumed = request.POST['update_amount_consumed']
                total_volume = request.POST['update_total_avail_volume']
                parse_date = parse(date_received)
                received_date = datetime.datetime.strftime(parse_date, '%Y-%m-%d')

                if amount_consumed != "" or  date_consumed != "" :
                    latest_vol = int(total_volume) - int(amount_consumed)
                    update_object = MongoConsumed.objects.filter(inventory_id=mongo_id).create(
                        mongo_id=generate_id(),
                        inventory_id_id=mongo_id,
                        date_consumed=date_consumed,
                        amount_consumed=amount_consumed,
                        total_avail_volume= int(total_volume)
                    )
                    if latest_vol != 0:
                        update_inventory = MongoInventory.objects.filter(id=mongo_id).update(
                            total_avail_volume=0,
                            batch_no=batch_no,
                            date_received=date_received
                        )
                        create_object = MongoInventory.objects.create(
                            mongo_id=generate_id(),
                            batch_no=batch_no,
                            date_received=received_date,
                            total_avail_volume=latest_vol
                        )
                    else:
                        update_inventory = MongoInventory.objects.filter(id=mongo_id).update(
                            total_avail_volume=0
                        )

                else:
                    update_inventory = MongoInventory.objects.filter(id=mongo_id).update(
                        total_avail_volume=total_volume,
                        batch_no=batch_no,
                        date_received=date_received
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


def edit_mongo_inventory(request):
    if request.method == 'POST':
        try:
            if request.method == 'POST':
                mongo_id = request.POST['edit_mongo_id']
                id = request.POST['edit_inventory_id']
                batch_no = request.POST['edit_batch_no']
                date_received = request.POST['edit_date_received']
                date_consumed = request.POST['edit_DateConsumed']
                amount_consumed = request.POST['edit_AmountConsumed']
                total_volume = request.POST['edit_total_avail_volume']
                parse_date = parse(date_received)
                received_date = datetime.datetime.strftime(parse_date, '%Y-%m-%d')

                latest_vol = int(total_volume) - int(amount_consumed)
                update_object = MongoConsumed.objects.filter(inventory_id=mongo_id).update(
                    inventory_id_id=mongo_id,
                    date_consumed=date_consumed,
                    amount_consumed=amount_consumed,
                    total_avail_volume=int(total_volume)
                )
                update_inventory = MongoInventory.objects.filter(id=mongo_id).update(
                    total_avail_volume=0,
                    batch_no=batch_no,
                    date_received=date_received
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
