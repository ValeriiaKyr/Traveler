from django.urls import path

from tours.models import CommentLocation
from tours.views import (
    index,
    LocationListView,
    TourListView,
    LocationDetailView,
    TourDetailView,
    TourCreateView,
    LocationCreateView,
    LocationUpdateView,
    TourUpdateView,
    LocationDeleteView,
    TourDeleteView,
    CommentLocationCreateView, CommentTourCreateView, RegistrationView

)

urlpatterns = [
    path("", index, name="index"),
    path("locations/", LocationListView.as_view(), name="locations-list"),
    path("locations/create/", LocationCreateView.as_view(), name="locations-create"),
    path("locations/<int:pk>/update/", LocationUpdateView.as_view(), name="locations-update"),
    path("locations/<int:pk>/delete/", LocationDeleteView.as_view(), name="locations-delete"),
    path("locations/<int:pk>/", LocationDetailView.as_view(), name="locations-detail"),
    path("tours/", TourListView.as_view(), name="tour-list"),
    path("tours/create/", TourCreateView.as_view(), name="tour-create"),
    path("tours/<int:pk>/", TourDetailView.as_view(), name="tour-detail"),
    path("tours/<int:pk>/delete/", TourDeleteView.as_view(), name="tour-delete"),
    path("tours/<int:pk>/update/", TourUpdateView.as_view(), name="tour-update"),
    path('locations/<int:pk>/add_comment/', CommentLocationCreateView.as_view(), name='add-comment'),
    path('tours/<int:pk>/add_comment/', CommentTourCreateView.as_view(), name='comment'),
    path('register/', RegistrationView.as_view(), name='register'),

]

app_name = "tours"
