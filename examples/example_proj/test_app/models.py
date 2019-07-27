from django.db import models

from dependency_app_fk.models import DepModFK
from dependency_app_m2m.models import DepModM2M
from dependency_app_o2o.models import DepModO2O


class TestObjA(models.Model):
    first_name = models.CharField(max_length=1, null=True)
    last_name = models.CharField(max_length=1, null=True)
    fk_dep = models.ForeignKey(DepModFK, on_delete=models.CASCADE, null=True)
    o2o_dep = models.OneToOneField(DepModO2O, on_delete=models.CASCADE, null=True)
    m2m_dep = models.ManyToManyField(DepModM2M)

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
