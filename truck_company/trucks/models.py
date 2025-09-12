from django.db import models
from .id_generator import id_generator

# Create your models here.
class Truck(models.Model):
    truck_code_number = models.CharField(max_length=12, unique=True, editable=False)
    truck_brand = models.CharField(max_length=20)
    truck_total_trips = models.PositiveBigIntegerField(default=0, null=False)


    def save(self, *args, **kwargs):
            if not self.truck_code_number:
                # Keep generating until unique
                new_id = id_generator.generate_identifier()
                while Truck.objects.filter(truck_code_number=new_id).exists():
                    new_id = id_generator.generate_identifier()
                self.truck_code_number = new_id
            super().save(*args, **kwargs)


    def __str__(self) -> str:
         return self.truck_code_number + " - " + self.truck_brand


    def increment_trips(self):
        self.truck_total_trips += 1
