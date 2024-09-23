from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from tours.models import Location, Tour, CommentLocation, CommentTour


class TourCreatForm(forms.ModelForm):
    location = forms.ModelMultipleChoiceField(
        queryset=Location.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Tour
        fields = "__all__"
        widgets = {
            "name":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "distance":
                forms.NumberInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "duration":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "place":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "description":
                forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;", "rows": 4
                    }
                ),
        }


class LocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"
        widgets = {
            "name":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "country":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "city":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "location":
                forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "opening_time":
                forms.TimeInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "closing_time":
                forms.TimeInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "price":
                forms.NumberInput(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;"
                    }
                ),
            "description":
                forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "style": "border: 1px solid #ccc;",
                        "rows": 4
                    }
                ),
        }


class CommentLocationForm(forms.ModelForm):
    class Meta:
        model = CommentLocation
        fields = ["body"]


class CommentTourForm(forms.ModelForm):
    class Meta:
        model = CommentTour
        fields = ["body"]


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
          'username',
          'email',
          'first_name',
          'last_name',
          'password1',
          'password2',
        )
