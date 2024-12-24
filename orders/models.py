from django.db import models
from products.models import ProductLine
from users.models import CustomUser as User
from users.models import Address
from .constants import STATUS_CHOICES, PENDING


class Order(models.Model):
    user = models.ForeignKey(
        User,
        related_name="orders",
        on_delete=models.CASCADE,
    )
    paid = models.BooleanField(
        default=False,
        editable=False,
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=PENDING,
    )
    payment_address = models.ForeignKey(
        Address,
        related_name="payments",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    shipping_address = models.ForeignKey(
        Address,
        related_name="shipments",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_total_cost(self):
        return sum(item.get_total_price() for item in self.items.all())

    @property
    def status_display(self):
        return STATUS_CHOICES.get(self.status, "UNKNOWN")


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE,
    )
    product_line = models.ForeignKey(
        ProductLine,
        related_name="order_items",
        on_delete=models.CASCADE,
    )
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product_line.price * self.quantity
