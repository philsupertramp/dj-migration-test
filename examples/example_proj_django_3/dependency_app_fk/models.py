from django.db import models


class DepModFK(models.Model):
    placeholder = models.BooleanField(default=True)
    new_field = models.BooleanField(default=True)


class ExtensionModel(models.Model):
    new_field = models.BooleanField(default=True)
