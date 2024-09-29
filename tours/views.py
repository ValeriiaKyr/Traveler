from typing import Any, Dict

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import FormView

from tours.forms import (
    TourCreateForm,
    LocationCreateForm,
    CommentLocationForm,
    CommentTourForm,
    LocationSearchForm,
    TourSearchForm,
    RegistrationForm
)
from tours.models import Tourist, Tour, Location


def index(request: HttpRequest) -> HttpResponse:
    num_tourists = Tourist.objects.count()
    num_loc = Location.objects.count()
    num_tour = Tour.objects.count()
    context = {
        "num_tourists": num_tourists,
        "num_loc": num_loc,
        "num_tour": num_tour,
    }
    return render(request, "index.html", context=context)


class LocationListView(generic.ListView):
    model = Location
    paginate_by = 6

    def get_context_data(self, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(LocationListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["location_search_form"] = LocationSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Location.objects.all()
        form = LocationSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class LocationDetailView(generic.DetailView):
    model = Location

class TourListView(generic.ListView):
    model = Tour
    paginate_by = 5

    def get_context_data(self, object_list=None, **kwargs) -> Dict[str, Any]:
        context = super(TourListView, self).get_context_data(**kwargs)
        place = self.request.GET.get("place", "")
        context["tour_search_form"] = TourSearchForm(
            initial={"place": place}
        )
        return context

    def get_queryset(self) -> QuerySet:
        queryset = Tour.objects.all()
        form = TourSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(place__icontains=form.cleaned_data["place"])
        return queryset


class TourDetailView(generic.DetailView):
    model = Tour


class TourCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tour
    form_class = TourCreateForm
    success_url = reverse_lazy("tours:tour-list")
    template_name = "tours/tour_form.html"


class LocationCreateView(LoginRequiredMixin, generic.CreateView):
    model = Location
    form_class = LocationCreateForm
    success_url = reverse_lazy("tours:locations-list")
    template_name = "tours/location_form.html"


class LocationUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Location
    form_class = LocationCreateForm
    success_url = reverse_lazy("tours:locations-list")
    template_name = "tours/location_form.html"


class TourUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tour
    form_class = TourCreateForm
    success_url = reverse_lazy("tours:tour-list")
    template_name = "tours/tour_form.html"


class LocationDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Location
    success_url = reverse_lazy("tours:locations-list")


class TourDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tour
    success_url = reverse_lazy("tours:tour-list")


class CommentLocationCreateView(LoginRequiredMixin, generic.CreateView):
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        location = get_object_or_404(Location, id=kwargs["pk"])
        form = CommentLocationForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.location = location
            comment.save()
            return redirect(location.get_absolute_url())
        return redirect(location.get_absolute_url())


class CommentTourCreateView(LoginRequiredMixin, generic.CreateView):
    def post(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        tour = get_object_or_404(Tour, id=kwargs["pk"])
        form = CommentTourForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.tour = tour
            comment.save()
            return redirect(tour.get_absolute_url())
        return redirect(tour.get_absolute_url())


class RegistrationView(FormView):
    template_name = "tours/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy("login")

    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in.")
            return redirect("tours:index")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form: Form) -> HttpResponse:
        user = form.save()
        login(self.request, user)
        messages.success(self.request, "Registration successful!")
        return super().form_valid(form)
