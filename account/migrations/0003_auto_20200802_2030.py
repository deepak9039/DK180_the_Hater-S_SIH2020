# Generated by Django 3.0 on 2020-08-02 15:00

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=account.models.get_image_name, verbose_name='Resume'),
        ),
    ]
