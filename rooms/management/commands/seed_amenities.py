from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):

    help = "This command creates amenities for rooms"

    def handle(self, *args, **options):
        amenities = [
            "Air Conditioning",
            "Alarm Clock",
            "Balcony",
            "Bathroom",
            "Bathtub",
            "Bed Linen",
            "Boating",
            "Cable TV",
            "Carbon Monoxide Detectors",
            "Chairs",
            "Children Area",
            "Coffee Maker in Room",
            "Cooking Hob",
            "Cookware & Kitchen Utensils",
            "Dishwasher",
            "Double Bed",
            "En Suite Bathroom",
            "Free Parking",
            "Free Wireless Internet",
            "Freezer",
            "Fridge / Freezer",
            "Golf",
            "Hair Dryer",
            "Heating",
            "Hot Tub",
            "Indoor Pool",
            "Ironing Board",
            "Microwave",
            "Outdoor Pool",
            "Outdoor Tennis",
            "Oven",
            "Queen Size Bed",
            "Restaurant",
            "Shopping Mall",
            "Shower",
            "Smoke Detectors",
            "Sofa",
            "Stereo",
            "Swimming pool",
            "Toilet",
            "Towels",
            "TV",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))