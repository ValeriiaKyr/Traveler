from unittest import TestCase

from tours.forms import TourSearchForm, LocationSearchForm, RegistrationForm


class FormTests(TestCase):
    def test_tour_search_form(self):
        form_data = {"place": "test"}
        form = TourSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["place"], "test")

    def test_location_search_form(self):
        form_data = {"name": "test"}
        form = LocationSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["name"], "test")

    def test_register_form(self):
        form_data = {
            "username": "test",
            "email": "test@test.com",
            "first_name": "test first",
            "last_name": "test last",
            "password1": "user12test",
            "password2": "user12test",
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
