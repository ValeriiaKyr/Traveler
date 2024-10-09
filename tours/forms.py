from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tours.models import (
    Location,
    Tour,
    Comment
)


class TourCreateForm(forms.ModelForm):
    location = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Tour
        fields = ["name", "distance", "duration", "place", "description", "location"]
        widgets = {
            "name":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "distance":
                forms.NumberInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "duration":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "place":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "description":
                forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "rows": 4
                    }
                ),
        }


class LocationCreateForm(forms.ModelForm):
    image = forms.ImageField(required=False, label="Add Image")

    class Meta:
        model = Location
        fields = ["name", "country", "city", "location", "opening_time", "closing_time", "price", "description", "image"]

        widgets = {
            "name":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "country":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "city":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "location":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "opening_time":
                forms.TimeInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "closing_time":
                forms.TimeInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "price":
                forms.NumberInput(
                    attrs={
                        "class": "form-control",
                    }
                ),
            "description":
                forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "rows": 4
                    }
                ),
        }


class LocationSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        ),
    )


class TourSearchForm(forms.Form):
    place = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by place"
            }
        ),
    )


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({"class": "form-control"})
            if self.errors.get(field_name):
                field.widget.attrs["class"] += " is-invalid"

    class Meta:
        model = get_user_model()
        fields = (
          "username",
          "email",
          "first_name",
          "last_name",
          "password1",
          "password2",
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
