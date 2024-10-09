import cloudinary.models
from django.contrib.auth.models import AbstractUser
from django.db import models
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
    image = cloudinary.models.CloudinaryField("image", null=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} in {self.country}, {self.city}"

    def get_absolute_url(self) -> str:
        return reverse("tours:locations-detail", args=[str(self.id)])


class Tourist(AbstractUser):
    class Meta:
        ordering = ["username"]

    def __str__(self) -> str:
        return self.username


class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    duration = models.TimeField()
    distance = models.FloatField(blank=True, null=True)
    location = models.ManyToManyField(Location, related_name="tours_location")
    place = models.CharField(max_length=255, default="Europe")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} - {self.place}"

    def get_absolute_url(self) -> str:
        return reverse("tours:tour-detail", args=[str(self.id)])


class Comment(models.Model):
    author = models.ForeignKey(
        Tourist,
        on_delete=models.CASCADE,
        related_name="comments_author"
    )
    body = models.TextField(verbose_name="Content")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="comments_location",
        null=True,
        blank=True
    )
    tour = models.ForeignKey(
        Tour,
        on_delete=models.CASCADE,
        related_name="comments_tour",
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        if self.location:
            return f"{self.author.username} - Location: {self.location.name}"
        elif self.tour:
            return f"{self.author.username} - Tour: {self.tour.name}"
