# Generated by Django 3.1.1 on 2020-09-26 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_auto_20200926_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='soil_assesment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculator.soilassessment'),
        ),
        migrations.AlterField(
            model_name='farminput',
            name='estimated_calculation',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
