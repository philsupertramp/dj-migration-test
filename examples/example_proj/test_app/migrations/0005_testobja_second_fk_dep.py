# Generated by Django 2.2.3 on 2019-07-27 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app_fk', '0003_extensionmodel'),
        ('test_app', '0004_auto_20190727_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='testobja',
            name='second_fk_dep',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dependency_app_fk.ExtensionModel'),
        ),
    ]