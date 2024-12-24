from django.contrib import admin

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    row_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = [
        "paid",
        "created_at",
        "updated_at",
    ]
    list_display = [
        "id",
        "user__email",
        "paid",
        "status",
    ]
    inlines = [OrderItemInline]
    readonly_fields = ["created_at"]
