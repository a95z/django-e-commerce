from users.models import CustomUser as User
from django.db import models
from django.urls import reverse
import uuid


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    parent = models.ForeignKey(
        "self",
        related_name="children",
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )
    level = models.PositiveIntegerField(default=0, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return self.name.capitalize()


class SeosanalEvents(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.capitalize()


class Product(models.Model):
    IN_STOCK = "IS"
    OUT_OF_STOCK = "OOS"
    BACK_ORDERED = "BO"

    STOCK_STATUS = {
        IN_STOCK: "In Stock",
        OUT_OF_STOCK: "Out of Stock",
        BACK_ORDERED: "Back Ordered",
    }
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        editable=False,
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    stock_status = models.CharField(
        choices=STOCK_STATUS,
        max_length=3,
        default=OUT_OF_STOCK,
    )
    category = models.ForeignKey(
        Category,
        related_name="products",
        on_delete=models.CASCADE,
    )
    seosonal_event = models.ForeignKey(
        SeosanalEvents,
        related_name="products",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("products:product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name.capitalize()


class Attribute(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name.capitalize()

    def __repr__(self):
        return self.name.capitalize()


class AttributeValue(models.Model):
    value = models.CharField(max_length=50)
    attribute = models.ForeignKey(
        Attribute,
        related_name="values",
        on_delete=models.RESTRICT,
    )

    def __str__(self):
        return self.value.capitalize()

    def __repr__(self):
        return self.value.capitalize()


class ProductLine(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.RESTRICT, related_name="product_lines"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    stock_qty = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    attributes = models.ManyToManyField(AttributeValue, related_name="product_lines")
    user = models.ForeignKey(
        User, on_delete=models.RESTRICT, editable=False, related_name="product_lines"
    )

    @property
    def name(self):
        attribute_values = [
            attribute.value.capitalize() for attribute in self.attributes.all()
        ]
        return f"{self.product.name}, {','.join(attribute_values)}"
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class ProductImage(models.Model):
    alt = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    image = models.ImageField()
    product_line = models.OneToOneField(
        ProductLine,
        on_delete=models.CASCADE,
        null=True,
        related_name="image",
    )

    @property
    def url(self):
        return self.image.url

    def save(self, *args, **kwargs):
        if not self.alt:
            self.alt = f"{self.product_line.product.name} image"

        super().save(*args, **kwargs)
