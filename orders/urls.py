from django.urls import path

from . import views

app_name = "orders"

urlpatterns = [
    path("", view=views.orders_list, name="orders"),
    path("create", view=views.order_create, name="order_create"),
    path("confirm/<order_id>", view=views.order_confirmation, name="order_confirm")
]
