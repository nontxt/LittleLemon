from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.PositiveSmallIntegerField(verbose_name='Number of guests')
    booking_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.title} : {self.price}'
