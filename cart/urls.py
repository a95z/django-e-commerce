from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("", view=views.cart_detail, name="cart_detail"),
    path("add/<int:product_line_id>", view=views.cart_add, name="cart_add"),
    path("remove/<int:product_line_id>", view=views.cart_remove, name="cart_remove"),
]
