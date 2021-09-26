from django.urls import path


from .views import *

app_name = "authentication"

urlpatterns = [
    path("accounts-table/", user_account_page, name="accounts_table")
]