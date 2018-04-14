# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 07:25
from __future__ import unicode_literals

from django.db import migrations, models
import part.models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0009_part_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='image',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to=part.models.rename_part_image),
        ),
    ]
