# Generated by Django 3.0 on 2020-03-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app_m2m', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depmodm2m',
            name='new_field',
            field=models.BooleanField(default=True),
        ),
    ]
