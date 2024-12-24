from django.urls import path
from . import views

app_name = "products"

urlpatterns = [
    path("", views.product_list, name="products_list"),
    path("search", views.product_search, name="product_search"),
    path("<int:product_line_id>", view=views.product_detail, name="product_detail"),
]
