# Generated by Django 3.1.1 on 2020-10-02 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20201002_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='farms',
            field=models.ManyToManyField(related_name='farmers_farms', to='calculator.Farm'),
        ),
    ]
