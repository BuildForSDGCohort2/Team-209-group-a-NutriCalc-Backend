from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.




class Fertilizer(models.Model):
    fertilizer_name = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    acres = models.IntegerField(default=0)
    amount_Nitrate = models.DecimalField(max_digits=4, decimal_places=2)
    amount_Phosphate = models.DecimalField(max_digits=4, decimal_places=2)
    amount_Potassium = models.DecimalField(max_digits=4, decimal_places=2)
    amount_Ammonium = models.DecimalField(max_digits=4, decimal_places=2)
    amount_Calcium = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        # string formating works on python3>>>
        return f'{self.fertilizer_name} - {self.amount_Nitrate}(N),{self.amount_Phosphate}(P),{self.amount_Potassium}(K),{self.amount_Ammonium}(NH4),{self.amount_Calcium}(Ca)'

class SoilAssessment(models.Model):
    # farm
    soil_type = models.DecimalField(max_digits=4, decimal_places=2)
    ph_value = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f'{self.soil_type}-{self.ph_value} pH'
    
class FertilizerAvailable(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    manufacture = models.CharField(max_length=200)
    class Meta:
        verbose_name_plural="Fertilizers available"
        
    def __str__(self):
        return f"{self.name}"

# Plant(nutrient_requirements,fertilizers,acidity,pproperties)
class Plant(models.Model):
    name = models.CharField(max_length=100)
    acidity = models.DecimalField(max_digits=2,decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - (pH {self.acidity})"

# FarmInput(plant,farmer,fertilizer,estimated_calculation)
class FarmInput(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=300)
    description = models.TextField()
    estimated_calculation = models.IntegerField(
        default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.fertilizer}-{self.purpose} ({self.estimated_calculation} kg per acre)"


class Area(models.Model):
    county = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.area_name}"
    

# Farm (farmer,name of farm,plant,soil_assesment,farm input)
class Farm(models.Model):
    name = models.CharField(max_length=100)
    acres = models.IntegerField(default=0)
    location = models.ForeignKey(Area, on_delete=models.CASCADE, related_name="place")
    soil_assesment = models.ForeignKey(
        SoilAssessment, on_delete=models.CASCADE, blank=True, null=True)
    farm_inputs = models.ManyToManyField(FarmInput, blank=True)
    plants = models.ManyToManyField(Plant, blank=True)

    def __str__(self):
        return f"{self.name},{self.location} -- {self.acres} acres"
# Farmer(plant,size_of_land,area)
class Farmer(models.Model):
    farm_owner=models.ForeignKey(get_user_model(),on_delete=models.CASCADE,related_name="_farmer")
    farms = models.ManyToManyField(Farm,related_name="farmers_farms")
    def __str__(self):
        number = self.farms.len()
        return f"{self.farm_owner} --{number} farms "
    
# Schedule(farmer,farm_input,date,farm_details,estimated calculation)
