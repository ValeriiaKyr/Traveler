from django import template

from tours.models import Tour

register = template.Library()


@register.filter
def join_locations(tour: Tour) -> str:
    return ", ".join([location.name for location in tour.location.all()])
