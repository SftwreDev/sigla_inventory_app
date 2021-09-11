from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.fried_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_fried_packed_inventory(request):

    if request.method == 'POST':
        try:
            id = request.POST['fried_id']
            batch_no = request.POST['update_batch_no']
            date_fried = request.POST['update_date_fried']

            update_object = FriedInventory.objects.filter(id=id).update(
                batch_no=batch_no,
                date_fried=date_fried,
            )

            return redirect("fried:fried_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
    return redirect('dashboard:dashboard')
