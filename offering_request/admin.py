from django.contrib import admin
from .models import Offering, Platform, PlatformOffering, Offering_request

# Register your models here.



admin.site.register(Offering)
admin.site.register(Platform)


class PlatformOfferingAdmin(admin.ModelAdmin):
    list_display = (
        'platform',
        'offering',
        'hide_fields',
    )

    list_editable = (
        'hide_fields',
    )
admin.site.register(PlatformOffering, PlatformOfferingAdmin)

admin.site.register(Offering_request)

