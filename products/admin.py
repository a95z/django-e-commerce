from django.contrib import admin
from .models import (
    Product,
    ProductLine,
    ProductImage,
    Category,
    Attribute,
    AttributeValue,
    SeosanalEvents,
)
import nested_admin


class CategoryInline(admin.StackedInline):
    model = Category
    extra = 0
    verbose_name = "Sub Category"
    verbose_name_plural = "Sub Categories"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]
    list_display = ["slug", "is_active", "get_parent"]
    prepopulated_fields = {"slug": ["name"]}

    def get_parent(self, obj):
        return obj.parent or None

    get_parent.short_description = "Parent"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(parent__isnull=True)


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    pass


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    pass


class ProductImageInline(nested_admin.NestedStackedInline):
    model = ProductImage
    extra = 0

class ProductLIneInline(nested_admin.NestedStackedInline):
    inlines = [ProductImageInline]
    model = ProductLine
    extra = 0


@admin.register(SeosanalEvents)
class SeosonalEventsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "start_date",
        "end_date",
    ]


@admin.register(Product)
class ProductAdmin(nested_admin.NestedModelAdmin):
    list_display = [
        "name",
        "category__name",
        "stock_status",
        "is_active",
    ]

    prepopulated_fields = {
        "slug": ["name"],
    }

    inlines = [ProductLIneInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.user = request.user
            instance.save()
        formset.save_m2m()
