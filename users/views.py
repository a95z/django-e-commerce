from django.contrib.auth import login, logout
from .forms import (
    CustomUserCreationForm as UserCreationForm,
    CustomAthenticationForm as AuthenticationForm,
)
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from cart.models import Cart


def sign_up(request):
    user = request.user

    if user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("products:products_list")
        return render(request, "users/sign_up.html", {"form": form})

    form = UserCreationForm()
    return render(request, "users/sign_up.html", {"form": form})


def sign_in(request):
    next = request.GET.get("next", "/")

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            try:
                cart = Cart.objects.get(user=user)
                request.session["cart_id"] = cart.id
            except Cart.DoesNotExist:
                pass

            return redirect(next)

        return render(
            request,
            "users/sign_in.html",
            {
                "form": form,
                "next": next,
            },
        )

    form = AuthenticationForm()
    return render(request, "users/sign_in.html", {"form": form, "next": next})


@require_POST
def sign_out(request):
    if not request.user.is_authenticated:
        return redirect("users:sign_in")

    if request.session.get("cart_id"):
        del request.session["cart_id"]

    logout(request)
    return redirect("users:sign_in")
