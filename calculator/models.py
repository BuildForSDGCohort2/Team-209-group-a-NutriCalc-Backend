from django.db import models

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
        return f'{self.fertilizer_name} - {self.amount_Nitrate}(N),{self.amount_Potassium}(K),{self.amount_Phosphate}(P),{self.amount_Ammonium}(NH4),{self.amount_Calcium}(Ca)' # string formating works on python3>>>

class SoilAssessment(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE)
    soil_type = models.DecimalField(max_digits=4, decimal_places=2)
    ph_value = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return f'{self.soil_type}-{self.ph_value} pH'
    
class FertilizerAvailable(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name