from django.db import models


class TestObjA(models.Model):
    first_name = models.CharField(max_length=1, null=True)
    last_name = models.CharField(max_length=1, null=True)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
