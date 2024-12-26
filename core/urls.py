from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve
from . import views

urlpatterns = [
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    path("admin/", admin.site.urls),
    path("about/", view=views.about_us),
    path("cart/", include("cart.urls", namespace="cart")),
    path("orders/", include("orders.urls", namespace="orders")),
    path("users/", include("users.urls", namespace="users")),
    path("", include("products.urls", namespace="products")),
]
