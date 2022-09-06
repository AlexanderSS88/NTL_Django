from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание')

class Measurement(models.Model):
    id = models.IntegerField(primary_key=True)
    temperature = models.DecimalField(decimal_places=0, max_digits=1, verbose_name='Температура')
    date = models.DateTimeField(auto_now=False, auto_now_add=False, editable=False, blank=True, verbose_name='Дата')
    image = models.ImageField(max_length=None, blank=True, null=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurement')

