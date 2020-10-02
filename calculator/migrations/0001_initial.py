# Generated by Django 3.1.1 on 2020-10-02 00:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('county', models.CharField(max_length=100)),
                ('area_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acres', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Fertilizer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilizer_name', models.CharField(max_length=200)),
                ('weight', models.IntegerField(default=0)),
                ('acres', models.IntegerField(default=0)),
                ('amount_Nitrate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount_Phosphate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount_Potassium', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount_Ammonium', models.DecimalField(decimal_places=2, max_digits=4)),
                ('amount_Calcium', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acidity', models.DecimalField(blank=True, decimal_places=2, max_digits=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SoilAssessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soil_type', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ph_value', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='FertilizerAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('manufacture', models.CharField(max_length=200)),
                ('fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.fertilizer')),
            ],
            options={
                'verbose_name_plural': 'Fertilizers available',
            },
        ),
        migrations.CreateModel(
            name='FarmInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('estimated_calculation', models.IntegerField(blank=True, default=0, null=True)),
                ('fertilizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.fertilizer')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('farms', models.ManyToManyField(to='calculator.Farm')),
            ],
        ),
        migrations.AddField(
            model_name='farm',
            name='farm_inputs',
            field=models.ManyToManyField(blank=True, to='calculator.FarmInput'),
        ),
        migrations.AddField(
            model_name='farm',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='place', to='calculator.area'),
        ),
        migrations.AddField(
            model_name='farm',
            name='plants',
            field=models.ManyToManyField(blank=True, to='calculator.Plant'),
        ),
        migrations.AddField(
            model_name='farm',
            name='soil_assesment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calculator.soilassessment'),
        ),
    ]
