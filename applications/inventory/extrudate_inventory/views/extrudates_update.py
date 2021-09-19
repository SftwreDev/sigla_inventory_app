from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.extrudate_inventory.models import *
from applications.base_settings.uuid_generator import *

def update_extrudate_inventory(request):

    if request.method == 'POST':
        try:
            if request.method == 'POST':
                id  = request.POST['extru_id']
                batch_no = request.POST['update_batch_no']
                total_volume = request.POST['update_total_volume']
                date_produced = request.POST['update_date_produced']
                batch_no_mongo = request.POST['update_batch_no_mongo']
                batch_no_rice = request.POST['update_batch_no_rice']
                batch_no_sesame = request.POST['update_batch_no_sesame']

                create_object = ExtruDateInventory.objects.filter(id=id).update(
                    batch_no=batch_no,
                    date_produced=date_produced,
                    total_volume=total_volume,
                    mongo_batch_no=batch_no_mongo,
                    rice_batch_no=batch_no_rice,
                    sesame_batch_no=batch_no_sesame
                )

                return redirect("extrudate:extrudate_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
        return redirect('dashboard:dashboard')