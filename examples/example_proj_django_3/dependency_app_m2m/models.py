from django.db import models


class DepModM2M(models.Model):
    placeholder = models.BooleanField(default=True)
    new_field = models.BooleanField(default=True)
