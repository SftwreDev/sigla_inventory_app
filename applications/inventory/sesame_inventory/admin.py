from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(SesameInventory)
admin.site.register(SesameConsumed)