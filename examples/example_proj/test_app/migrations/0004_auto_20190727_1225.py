# Generated by Django 2.2.3 on 2019-07-27 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app_m2m', '0001_initial'),
        ('dependency_app_fk', '0001_initial'),
        ('dependency_app_o2o', '0001_initial'),
        ('test_app', '0003_remove_testobja_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='testobja',
            name='fk_dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dependency_app_fk.DepModFK'),
        ),
        migrations.AddField(
            model_name='testobja',
            name='m2m_dep',
            field=models.ManyToManyField(to='dependency_app_m2m.DepModM2M'),
        ),
        migrations.AddField(
            model_name='testobja',
            name='o2o_dep',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='dependency_app_o2o.DepModO2O'),
        ),
    ]