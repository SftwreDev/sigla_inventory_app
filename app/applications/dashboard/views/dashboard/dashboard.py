from django.shortcuts import render, redirect

from applications.mongo_inventory.views.mongo_list import *

def dashboard_page(request):
    """
        Function for creating dashboard page
    """
    template_name = "dashboard/dashboard.html"


    return render(request, template_name)