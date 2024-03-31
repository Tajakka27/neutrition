from django.contrib import admin

# Register your models here.
from home.models import *
from datetime import datetime, timedelta
from django.utils import timezone
from rangefilter.filters import (
    DateRangeFilterBuilder,
    DateTimeRangeFilterBuilder,
    NumericRangeFilterBuilder,
    DateRangeQuickSelectListFilterBuilder,
)

import csv
from django.http import HttpResponse

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_date','cause')
    search_fields = ['name', 'phone', 'email','cause']
    list_filter = (
        ("created_date", DateRangeQuickSelectListFilterBuilder()),  # Filter by date range
        # Additional quick select options
    )
    def change_view(self, request, object_id, form_url='', extra_context=None):
            extra_context = extra_context or {}
            extra_context['show_export_button'] = True
            return super().change_view(request, object_id, form_url=form_url, extra_context=extra_context)

    def export_to_csv(self, request, queryset):
        try:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="filtered_data.csv"'
            
            writer = csv.writer(response)
            writer.writerow(['Name', 'Email', 'Phone', 'Created Date'])
            
            for obj in queryset:
                writer.writerow([obj.name, obj.email, obj.phone, obj.created_date])
            
            return response
        except Exception as e:
            # Log the exception or print an error message for debugging
            print(f"Error exporting CSV: {e}")
            # You can also return a custom error response if needed
            return HttpResponse("An error occurred during CSV export.")

    export_to_csv.short_description = "Export selected records to CSV"
    actions = ['export_to_csv']
admin.site.register(Appointment, AppointmentAdmin)


@admin.register(SiteDescription)
class SiteDescriptionAdmin(admin.ModelAdmin):
    list_display = ('motto', 'email', 'phone')  # Display these fields in the list view
    
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('image', 'review')   # No need to customize the admin interface for now


@admin.register(AvailableTime)
class AvailableTimeAdmin(admin.ModelAdmin):
    list_display = ('day', 'start_time', 'end_time')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')



