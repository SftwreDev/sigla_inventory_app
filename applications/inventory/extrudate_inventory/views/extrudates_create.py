from django.shortcuts import redirect, render

from applications.inventory.extrudate_inventory.models import *


def add_extrudate_inventory(request):

    if request.method == 'POST':
        try:
            template = "dashboard/mongo/mongo_js.html"
            batch_no = request.POST['batch_no']
            total_volume = request.POST['total_volume']
            date_produced = request.POST['date_produced']
            batch_no_mongo = request.POST['batch_no_mongo']
            batch_no_rice = request.POST['batch_no_rice']
            batch_no_sesame = request.POST['batch_no_sesame']

            create_object = ExtruDateInventory.objects.create(
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
