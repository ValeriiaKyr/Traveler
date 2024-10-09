from django.contrib.auth import get_user_model
from django.test import TestCase

from tours.models import Tour, Location, Comment


class ModelsTests(TestCase):
    def test_tour_str(self):
        location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )

        tour = Tour.objects.create(
            name="test",
            duration="2:00",
            place="test",
        )
        tour.location.add(location)
        self.assertEqual(str(tour), f"{tour.name} - {tour.place}")

    def test_location_str(self):
        location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )
        self.assertEqual(
            str(location),
            f"{location.name} in {location.country}, {location.city}"
        )

    def test_tourist_str(self):
        tourist = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(
            str(tourist),
            f"{tourist.username}"
        )

    def test_comment_location_str(self):
        location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )
        tourist = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )

        comment = Comment.objects.create(
            location=location,
            author=tourist,
            body="test",
            active=True,
        )

        self.assertEqual(
            str(comment),
            f"{comment.author.username} - Location: {comment.location.name}"
        )

    def test_comment_tour_str(self):
        location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )

        tour = Tour.objects.create(
            name="test",
            duration="2:00",
            place="test",
        )
        tour.location.add(location)

        tourist = get_user_model().objects.create(
            username="test",
            password="test123",
            first_name="test_first",
            last_name="test_last",
        )

        comment = Comment.objects.create(
            tour=tour,
            author=tourist,
            body="test",
            active=True,
        )
        self.assertEqual(
            str(comment),
            f"{comment.author.username} - Tour: {comment.tour.name}"
        )
