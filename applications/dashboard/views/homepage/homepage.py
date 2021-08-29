from django.shortcuts import render, redirect




def homepage(request):
    """
        Function for homepage
    """
    template_name = "homepage/homepage.html"

    return render(request, template_name)