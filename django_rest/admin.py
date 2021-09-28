from django.contrib import admin
from .models import meterReadings
# Register your models here.
class restAdmin(admin.ModelAdmin):
    list_display = ('house','flat','choicesMater','metRadings')


admin.site.register(meterReadings,restAdmin)
