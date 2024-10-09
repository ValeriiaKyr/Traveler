from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from tours.models import Tour, Location, Tourist


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ["name", "duration"]
    list_filter = ["name"]
    search_fields = ["name"]


@admin.register(Tourist)
class TouristAdmin(UserAdmin):
    list_display = UserAdmin.list_display


admin.site.register(Location)
