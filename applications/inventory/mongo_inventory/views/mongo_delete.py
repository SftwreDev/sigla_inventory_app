from django.shortcuts import redirect, render
import datetime
from django.db.models import Sum
from dateutil.parser import parse
from applications.inventory.mongo_inventory.models import *
from applications.base_settings.uuid_generator import *

def delete_mongo_inventory(request):

    if request.method == 'POST':
        try:
            if request.method == 'POST':
                mongo_id = request.POST['delete_mongo_id']
                id = request.POST['delete_inventory_id']
                update_inventory = MongoInventory.objects.filter(id=mongo_id).delete()

                return redirect("mongo:mongo_list")
        except Exception as e:
            print(e)
            context = {
                "error": e
            }
            error_template = "error.html"
            return render(request, error_template, context)
    return redirect('dashboard:dashboard')