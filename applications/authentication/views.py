from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.contrib.auth import login

from .models import *
from .forms import *

class StaffSignUpView(CreateView):
    model = User
    form_class = StaffForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'staff'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("/")

@login_required(login_url='/app/v1/accounts/login/')
def user_account_page(request):
    template_name = "authentication/account_table.html"

    user = User.objects.all()
    form = StaffForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("authentication:accounts_table")
    
    else:
        form = StaffForm(request.POST or None)

    context = {
        "user": user,
        "form" : form,
    }

    return render(request, template_name, context=context)
