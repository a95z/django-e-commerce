from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser as User, Address


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0
    verbose_name_plural = "addresses"


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [AddressInline]

    # Specify which fields to display when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone",)}),  # Add custom fields
    )

    # Specify which fields to display when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone",)}),  # Add custom fields for user creation
    )
