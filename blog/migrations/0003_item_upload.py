# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-26 15:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='upload',
            field=models.FileField(default=django.utils.timezone.now, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
