# Generated by Django 4.1 on 2022-09-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='date',
            field=models.DateTimeField(blank=True, editable=False, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='measurement',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
