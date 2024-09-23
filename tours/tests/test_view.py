from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client


from tours.models import Tour, Location

LOCATION_URL = reverse('tours:locations-list')
TOUR_URL = reverse('tours:tour-list')

class TourTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_tour(self):
        location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )

        tour1 = Tour.objects.create(
            name="test1",
            duration="2:00",
            place="test1",
            # location=location,
        )
        tour2 = Tour.objects.create(
            name="test2",
            duration="2:00",
            place="test2",
            # location=location,
        )
        tour1.location.add(location)
        tour2.location.add(location)
        response = self.client.get(TOUR_URL)
        self.assertEqual(response.status_code, 200)
        tour_queryset = Tour.objects.all()
        self.assertEqual(
            list(response.context["tour_list"]),
            list(tour_queryset)
        )
        self.assertTemplateUsed(response, 'tours/tour_list.html')


class LocationsTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_tour(self):
        location1 = Location.objects.create(
            name="test1",
            country="test1",
            city="test1",
            location="test1",
            price="10.00"
        )

        location2 = Location.objects.create(
            name="test2",
            country="test2",
            city="test2",
            location="test2",
            price="10.00"
        )

        response = self.client.get(LOCATION_URL)
        self.assertEqual(response.status_code, 200)
        location_queryset = Location.objects.all()
        self.assertEqual(
            list(response.context["location_list"]),
            list(location_queryset)
        )
        self.assertTemplateUsed(response, 'tours/location_list.html')

