from django.db import models


class Table(models.Model):
    regulator = models.TextField(verbose_name="Regulator")
    link = models.URLField(max_length=500)
    description = models.TextField(verbose_name="description")
    date = models.DateTimeField(auto_now_add=False, blank=True)
