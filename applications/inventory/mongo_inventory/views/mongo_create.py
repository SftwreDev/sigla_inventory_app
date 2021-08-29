from django.shortcuts import redirect, render

from applications.inventory.mongo_inventory.models import *


def add_mongo_inventory(request):

    if request.method == 'POST':
        try:
            template = "dashboard/mongo/mongo_js.html"
            batch_no = request.POST['batch_no']
            total_avail_volume = request.POST['total_avail_volume']
            date_received = request.POST['date_received']

            create_object = MongoInventory.objects.create(
                batch_no=batch_no, date_received=date_received,
                total_avail_volume=total_avail_volume
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
