from django.contrib import admin

# Register your models here.
from home.models import *
# admin.site.register(Appointment)


@admin.register(Appointment)
class   PostAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "time")


@admin.register(PersonalInformation)
class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('motto', 'email', 'phone')  # Display these fields in the list view
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image', 'review')   # No need to customize the admin interface for now


@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time')