from django.contrib import admin
from .models import Fertilizer, SoilAssessment, FertilizerAvailable, Farmer, Farm, FarmInput,  Plant, Area

# Register your models here.

admin.site.register(Fertilizer)
admin.site.register(FertilizerAvailable)
admin.site.register(SoilAssessment)
admin.site.register(Plant)
admin.site.register(FarmInput)
admin.site.register(Farm)
admin.site.register(Farmer)
admin.site.register(Area)

