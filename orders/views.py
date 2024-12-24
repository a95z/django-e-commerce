from django.shortcuts import render, redirect, get_object_or_404
from .models import Order, OrderItem
from cart.models import Cart
from core.utils import redirect_with_params
from users.forms import AddressCreationForm
from users.models import Address


def order_create(request):
    user = request.user
    full_path = request.get_full_path()

    if not user.is_authenticated:
        return redirect_with_params("users:sign_in", next=full_path)

    if request.method == "POST":
        if not user.addresses.exists():
            form = AddressCreationForm(data=request.POST)

            if form.is_valid():
                address = form.save(commit=False)
                address.user = user
                address.save()
            else:
                return render(
                    request,
                    "orders/order_create.html",
                    {
                        "form": form,
                    },
                )
        else:
            cart = Cart.objects.get(user=user)

            if not cart.items.exists():
                return redirect("car:cart_detail")

            address = Address.objects.get(user=user, is_default=True)

            order = Order.objects.create(user=user, shipping_address=address)

            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product_line=item.product_line,
                    quantity=item.quantity,
                )

            cart.delete()

            return redirect("orders:order_confirm", order_id=order.id)


def order_confirmation(request, order_id):
    user = request.user

    if not user.is_authenticated:
        redirect_with_params("user:sign_in")

    order = get_object_or_404(Order, id=order_id)

    return render(
        request=request,
        template_name="orders/order_confirm.html",
        context={
            "order": order,
        },
    )


def orders_list(request):
    full_path = request.get_full_path()
    user = request.user

    if not user.is_authenticated:
        return redirect_with_params("users:sign_in", next=full_path)

    orders = Order.objects.filter(user=user)

    return render(
        request=request,
        template_name="orders/order_list.html",
        context={
            "orders": orders,
        },
    )
