from django.contrib import admin
from pagedown.widgets import AdminPagedownWidget

from .models import Site, Tariff, SiteInTariff, Profile, Dogovor
from django.db import models

# Register your models here.
class TariffAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
admin.site.register(Site)
admin.site.register(SiteInTariff)
admin.site.register(Tariff, TariffAdmin)
admin.site.register(Profile)
admin.site.register(Dogovor)