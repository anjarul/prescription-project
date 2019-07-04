from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Prescription


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ['id', 'patient_name', 'prescription_date', 'patient_age',
                    'patient_gender', 'diagnosis', 'medicines', 'next_visit_date', 'user']

    list_display_links = ['patient_name']

    search_fields = ['patient_name']

    # filter_horizontal = ['user']

    # list_filter = ['prescription_date', 'patient_name', ]
    list_filter = (
        ('prescription_date', DateRangeFilter),
    )


admin.site.register(Prescription, PrescriptionAdmin)
