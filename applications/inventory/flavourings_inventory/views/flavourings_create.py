from django.shortcuts import redirect, render

from applications.inventory.flavourings_inventory.models import *


def add_flavourings_inventory(request):

    if request.method == 'POST':
        try:
            batch_no = request.POST['batch_no']
            flavourings = request.POST['flavourings']
            total_avail_volume = request.POST['total_avail_volume']
            date_received = request.POST['date_received']

            create_object = FlavouringsInventory.objects.create(
                batch_no=batch_no,
                flavourings=flavourings,
                total_avail_volume=total_avail_volume,
                date_received=date_received,
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
