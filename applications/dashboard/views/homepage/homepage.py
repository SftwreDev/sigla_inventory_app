from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



@login_required(login_url='/app/v1/accounts/login/')
def homepage(request):
    """
        Function for homepage
    """
    template_name = "homepage/homepage.html"

    return render(request, template_name)