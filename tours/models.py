from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.conf import settings
from django.urls import reverse


class Location(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    opening_time = models.TimeField(blank=True, null=True)
    closing_time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='static/images/', blank=True, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} in {self.country}, {self.city}"

    def get_absolute_url(self):
        return reverse("tours:locations-detail", args=[str(self.id)])


class Tourist(AbstractUser):
    class Meta:
        ordering = ['username']


    def __str__(self):
        return self.username


class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.TimeField()
    distance = models.FloatField(blank=True, null=True)
    location = models.ManyToManyField(Location, related_name='tours_location')
    place = models.CharField(max_length=255, default="Europe")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name} - {self.place}"

    def get_absolute_url(self):
        return reverse("tours:tour-detail", args=[str(self.id)])

class CommentLocation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='Content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author.username} - {self.location.name}'


class CommentTour(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='tour_comments')
    author = models.ForeignKey(Tourist, on_delete=models.CASCADE, related_name='tour_comments')
    body = models.TextField(verbose_name='Content')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.author.username} - {self.tour.name}'