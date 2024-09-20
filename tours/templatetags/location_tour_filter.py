from django import template


register = template.Library()


@register.filter
def join_locations(tour):
    return ", ".join([location.name for location in tour.location.all()])