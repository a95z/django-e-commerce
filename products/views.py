from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from .models import Category, ProductLine
from cart.models import Cart
from core.utils import make_breadcrumbs
from django.http import Http404


def product_list(request):
    full_path = request.get_full_path()
    user = request.user
    cart_id = request.session.get("cart_id")
    category_slug = request.GET.get("category")

    category = None

    categories = Category.objects.annotate(products_count=Count("products"))

    product_lines = ProductLine.objects.filter(is_active=True)

    if user.is_authenticated:
        cart = Cart.objects.filter(Q(id=cart_id) | Q(user=user)).first()
    else:
        cart = Cart.objects.filter(id=cart_id).first()

    if category_slug:
        category = Category.objects.get(slug=category_slug)
        product_lines = product_lines.filter(product__category=category)

    context = {
        "products": list(product_lines),
        "active_category": category,
        "categories": categories,
        "cart": cart,
    }

    if category:
        context["breadcrumbs"] = make_breadcrumbs(full_path)

    return render(
        request=request,
        template_name="products/product_list.html",
        context=context,
    )


def product_detail(request, product_line_id):
    try:
        product_line = ProductLine.objects.get(
            id=product_line_id,
            is_active=True,
        )
        related_products = ProductLine.objects.filter(
            product__category=product_line.product.category,
            is_active=True,
        ).exclude(id=product_line.id)

        context = {
            "product": product_line,
            "related_products": related_products,
        }

        return render(
            request=request,
            template_name="products/product_detail.html",
            context=context,
        )
    except ProductLine.DoesNotExist:
        raise Http404("Product Not Found")


def product_search(request):
    full_path = request.get_full_path()

    term = request.GET.get("term")

    product_lines = None

    if term:
        product_lines = ProductLine.objects.filter(
            Q(product__name__contains=term) | Q(product__category__name__contains=term),
        )

    context = {
        "term": term,
        "products": product_lines,
        "breadcrumbs": make_breadcrumbs(full_path=full_path),
    }

    return render(request, "products/product_search.html", context=context)
