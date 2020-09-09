from django.contrib import admin
from .models import Fertilizer, SoilAssessment, FertilizerAvailable

# Register your models here.

admin.site.register(Fertilizer)
admin.site.register(FertilizerAvailable)
admin.site.register(SoilAssessment)
