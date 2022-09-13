from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, blank=True, verbose_name='Описание')


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name='Температура')
    date = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False, blank=True, verbose_name='Дата')
    image = models.ImageField(max_length=None, blank=True, null=True)


