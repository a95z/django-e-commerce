from django.core.management.base import BaseCommand
from products.models import Category
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Seeds the database with predefined categories."

    def handle(self, *args, **kwargs):
        categories = [
            {
                "name": "Electronics",
                "slug": slugify("Electronics"),
                "is_active": True,
                "level": 0,
                "parent": None,
                "description": "Find the latest and greatest in tech gadgets and devices.",
            },
            {
                "name": "Smartphones",
                "slug": slugify("Smartphones"),
                "is_active": True,
                "level": 1,
                "parent": "Electronics",
                "description": "Shop the newest smartphones from top brands.",
            },
            {
                "name": "Laptops",
                "slug": slugify("Laptops"),
                "is_active": True,
                "level": 1,
                "parent": "Electronics",
                "description": "Discover laptops for work, play, and everything in between.",
            },
            {
                "name": "Home Appliances",
                "slug": slugify("Home Appliances"),
                "is_active": True,
                "level": 0,
                "parent": None,
                "description": "Upgrade your home with modern appliances.",
            },
            {
                "name": "Kitchen Appliances",
                "slug": slugify("Kitchen Appliances"),
                "is_active": True,
                "level": 1,
                "parent": "Home Appliances",
                "description": None,
            },
            {
                "name": "Furniture",
                "slug": slugify("Furniture"),
                "is_active": True,
                "level": 0,
                "parent": None,
                "description": "Stylish and functional furniture for every room.",
            },
            {
                "name": "Office Furniture",
                "slug": slugify("Office Furniture"),
                "is_active": True,
                "level": 1,
                "parent": "Furniture",
                "description": "Ergonomic office furniture to enhance productivity.",
            },
            {
                "name": "Books",
                "slug": slugify("Books"),
                "is_active": True,
                "level": 0,
                "parent": None,
                "description": "A world of knowledge and stories awaits.",
            },
            {
                "name": "Fiction",
                "slug": slugify("Fiction"),
                "is_active": True,
                "level": 1,
                "parent": "Books",
                "description": None,
            },
            {
                "name": "Non-Fiction",
                "slug": slugify("Non-Fiction"),
                "is_active": True,
                "level": 1,
                "parent": "Books",
                "description": "Expand your understanding with factual books.",
            },
        ]

        created_categories = {}

        for data in categories:
            parent = created_categories.get(data["parent"]) if data["parent"] else None
            category = Category.objects.create(
                name=data["name"],
                slug=data["slug"],
                is_active=data["is_active"],
                level=data["level"],
                parent=parent,
                description=data.get("description"),
            )
            created_categories[data["name"]] = category

        self.stdout.write(self.style.SUCCESS("Categories created successfully!"))
