# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 08:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import part.models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0010_auto_20180414_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attachment', models.FileField(blank=True, null=True, upload_to=part.models.attach_file)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='part.Part')),
            ],
        ),
    ]
