"""main_settings URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('app/v1/accounts/', include('django.contrib.auth.urls')),

    path('', include('applications.dashboard.urls.homepage_urls')),
    path('app/v1/', include('applications.dashboard.urls.dashboard_urls')),
    path('app/v1/', include('applications.inventory.mongo_inventory.urls')),
    path('app/v1/', include('applications.inventory.rice_inventory.urls')),
    path('app/v1/', include('applications.inventory.sesame_inventory.urls')),
    path('app/v1/', include('applications.inventory.extrudate_inventory.urls')),
    path('app/v1/', include('applications.inventory.market_inventory.urls')),
    path('app/v1/', include('applications.inventory.fried_inventory.urls')),
    path('app/v1/', include('applications.inventory.flavourings_inventory.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
