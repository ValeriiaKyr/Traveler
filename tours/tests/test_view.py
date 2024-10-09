from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tours.models import Tour, Location, Comment

LOCATION_URL = reverse("tours:locations-list")
TOUR_URL = reverse("tours:tour-list")
# COMMENT_LOCATION_URL = reverse("tours:add-location-comment", kwargs={"location_id": location.id})
# COMMENT_TOUR_URL = reverse("tours:add-tour-comment", kwargs={"pk": 1})
REGISTRATION_URL = reverse("tours:register")


class TourTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_tour(self) -> None:
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
        )
        tour2 = Tour.objects.create(
            name="test2",
            duration="2:00",
            place="test2",
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
        self.assertTemplateUsed(response, "tours/tour_list.html")


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
        self.assertTemplateUsed(response, "tours/location_list.html")

class CommentLocationTests(TestCase):
    def setUp(self)-> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )
        self.client.force_login(self.user)


    def test_create_comment_for_location(self) -> None:
        form_data = {
            "body": "test"
        }
        response = self.client.post(
            # COMMENT_LOCATION_URL,
            reverse("tours:add-location-comment", kwargs={"location_id": self.location.id}),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(location=self.location, author=self.user, body="test").exists())


class CommentTourTests(TestCase):
    def setUp(self)-> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="test123"
        )
        self.location = Location.objects.create(
            name="test",
            country="test",
            city="test",
            location="test",
            price="10.00"
        )
        self.tour = Tour.objects.create(
            name="test1",
            duration="2:00",
            place="test1",
        )
        self.client.force_login(self.user)


    def test_create_comment_for_location(self) -> None:
        form_data = {
            "body": "test"
        }
        response = self.client.post(
            reverse("tours:add-tour-comment", kwargs={"tour_id": self.tour.id}),
            data=form_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(tour=self.tour, author=self.user, body="test").exists())


class RegistrationViewTests(TestCase):
    def test_registration_success(self):
        response = self.client.post(REGISTRATION_URL, {
            "username": "user",
            "password1": "testpassword123",
            "password2": "testpassword123",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(get_user_model().objects.filter(username="user").exists())
