from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import *

class StaffForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_staff = True
        user.save()
        staff = Staff.objects.create(user=user)
        return user