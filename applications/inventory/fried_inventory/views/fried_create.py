from django.shortcuts import redirect, render

from applications.inventory.fried_inventory.models import *


def add_fried_packed_inventory(request):

    if request.method == 'POST':
        try:
            batch_no = request.POST['batch_no']
            date_fried = request.POST['date_fried']

            create_object = FriedInventory.objects.create(
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
