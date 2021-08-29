from django.urls import path



from applications.dashboard.views.homepage.homepage import *


app_name = "homepage"

urlpatterns = [
    path("" , homepage, name="homepage"),
]