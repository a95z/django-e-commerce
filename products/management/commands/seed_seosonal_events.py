from django.core.management.base import BaseCommand
from products.models import SeosanalEvents
from datetime import datetime
from django.utils import timezone


class Command(BaseCommand):
    help = "Seeds the database with predefined seasonal events."

    def handle(self, *args, **kwargs):
        seosanal_events = [
            {
                "name": "Winter Sale",
                "start_date": timezone.make_aware(datetime(2024, 12, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2024, 12, 31, 23, 59)),
            },
            {
                "name": "Black Friday Deals",
                "start_date": timezone.make_aware(datetime(2024, 11, 29, 0, 0)),
                "end_date": timezone.make_aware(datetime(2024, 11, 29, 23, 59)),
            },
            {
                "name": "Spring Clearance",
                "start_date": timezone.make_aware(datetime(2025, 3, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2025, 3, 31, 23, 59)),
            },
            {
                "name": "Summer Sale",
                "start_date": timezone.make_aware(datetime(2025, 6, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2025, 6, 30, 23, 59)),
            },
            {
                "name": "Holiday Promotions",
                "start_date": timezone.make_aware(datetime(2024, 12, 15, 0, 0)),
                "end_date": timezone.make_aware(datetime(2024, 12, 25, 23, 59)),
            },
            {
                "name": "Back to School Discounts",
                "start_date": timezone.make_aware(datetime(2025, 8, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2025, 8, 31, 23, 59)),
            },
            {
                "name": "Cyber Monday Deals",
                "start_date": timezone.make_aware(datetime(2024, 12, 2, 0, 0)),
                "end_date": timezone.make_aware(datetime(2024, 12, 2, 23, 59)),
            },
            {
                "name": "Valentine's Day Special",
                "start_date": timezone.make_aware(datetime(2025, 2, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2025, 2, 14, 23, 59)),
            },
            {
                "name": "Autumn Festival",
                "start_date": timezone.make_aware(datetime(2025, 10, 1, 0, 0)),
                "end_date": timezone.make_aware(datetime(2025, 10, 31, 23, 59)),
            },
            {
                "name": "New Year's Eve Sale",
                "start_date": timezone.make_aware(datetime(2024, 12, 31, 0, 0)),
                "end_date": timezone.make_aware(datetime(2024, 12, 31, 23, 59)),
            },
        ]

        for event in seosanal_events:
            SeosanalEvents.objects.create(
                name=event["name"],
                start_date=event["start_date"],
                end_date=event["end_date"],
            )

        self.stdout.write(self.style.SUCCESS("Seasonal events created successfully!"))
