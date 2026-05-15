from django.db import models

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField()

    def vehicle_info(self):
        return f"{self.brand} costs {int(self.price)}"

class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        return f"{self.brand} Car with {self.doors} doors costs {int(self.price)}"

class Motorcycle(Vehicle):
    helmet_included = models.BooleanField()

    def vehicle_info(self):
        return f"{self.brand} Motorcycle costs {int(self.price)}"
