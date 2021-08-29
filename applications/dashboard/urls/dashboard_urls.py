from django.urls import path



from applications.dashboard.views.dashboard.dashboard import *


app_name = "dashboard"

urlpatterns = [
    path("dashboard/" , dashboard_page, name="dashboard"),
]