# Generated by Django 4.1 on 2022-09-10 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0003_alter_measurement_date_alter_measurement_temperature'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor',
            new_name='sensor_id',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(verbose_name='Температура'),
        ),
    ]
