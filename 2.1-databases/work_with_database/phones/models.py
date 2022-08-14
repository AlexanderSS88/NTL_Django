from django.db import models
from slugify import slugify
import csv


class Phone(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(max_length=80, verbose_name="URL")
    price = models.CharField(max_length=20)
    image = models.CharField(max_length=150)
    release_date = models.CharField(max_length=150)
    lte_exists = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
