from django.db import models

from dependency_app_fk.models import DepModFK, ExtensionModel
from dependency_app_m2m.models import DepModM2M
from dependency_app_o2o.models import DepModO2O
from django.dispatch import receiver

from test_app.signals import test_signal


class TestObjA(models.Model):
    first_name = models.CharField(max_length=1, null=True)
    last_name = models.CharField(max_length=1, null=True)
    fk_dep = models.ForeignKey(DepModFK, on_delete=models.CASCADE, null=True)
    second_fk_dep = models.ForeignKey(ExtensionModel, on_delete=models.CASCADE, null=True)
    o2o_dep = models.OneToOneField(DepModO2O, on_delete=models.CASCADE, null=True)
    m2m_dep = models.ManyToManyField(DepModM2M)
    call_count = models.IntegerField(default=0)

    @property
    def name(self):
        name = f'{self.first_name} {self.last_name}'
        test_signal.send_robust(sender=self.__class__, instance=self, test_arg=name)
        return name


@receiver(test_signal, sender=TestObjA)
def some_additional_action(sender, instance, test_arg, **kwargs):
    instance.call_count += 1
    instance.save(update_fields=['call_count'])
