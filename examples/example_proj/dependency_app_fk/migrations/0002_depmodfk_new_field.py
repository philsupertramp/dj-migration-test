# Generated by Django 2.2.3 on 2019-07-27 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dependency_app_fk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='depmodfk',
            name='new_field',
            field=models.BooleanField(default=True),
        ),
    ]
