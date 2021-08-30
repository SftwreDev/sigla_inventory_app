"""main_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),


    path('app/v1/accounts/', include('django.contrib.auth.urls')),

    path('', include('applications.dashboard.urls.homepage_urls')),
    path('app/v1/', include('applications.dashboard.urls.dashboard_urls')),
    path('app/v1/', include('applications.mongo_inventory.urls')),
]
