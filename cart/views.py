from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from products.models import ProductLine
from cart.models import Cart, CartItem


@require_POST
def cart_add(request, product_line_id):
    user = request.user
    next = request.GET.get("next")
    cart_id = request.session.get("cart_id")

    if user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=user)
        if created:
            cart.user = user
            request.session["cart_id"] = cart.id
    else:
        cart, created = Cart.objects.get_or_create(id=cart_id)
        if created:
            request.session["cart_id"] = cart.id

    product_line = get_object_or_404(ProductLine, id=product_line_id)

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart, product_line=product_line
    )

    if not created:
        cart_item.quantity += 1

    cart_item.save()

    if user.is_authenticated:
        cart.save()

    if next == "cart":
        return redirect("cart:cart_detail")

    response_data = {
        "success": True,
        "message": f"Added {product_line.name} to cart.",
        "product_id": product_line_id,
    }

    return JsonResponse(response_data)


def cart_detail(request):
    user = request.user
    cart_id = request.session.get("cart_id")

    if user.is_authenticated:
        cart = Cart.objects.filter(Q(id=cart_id) | Q(user=user)).first()
    else:
        cart = Cart.objects.filter(id=cart_id).first()

    return render(
        request=request,
        template_name="cart/cart_detail.html",
        context={
            "cart": cart,
        },
    )


@require_POST
def cart_remove(request, product_line_id):
    user = request.user
    cart_id = request.session.get("cart_id")

    if user.is_authenticated:
        cart = get_object_or_404(Cart, Q(id=cart_id) | Q(user=user))
    else:
        cart = get_object_or_404(Cart, id=cart_id)

    item = get_object_or_404(CartItem, product_line__id=product_line_id, cart=cart)

    item.delete()

    return redirect("cart:cart_detail")
