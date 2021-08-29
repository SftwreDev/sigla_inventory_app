from django.db import models



class BaseModel(models.Model):
    created_by = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
