# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-13 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_auto_20160608_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='last_update_data_source_version_hash',
            field=models.CharField(default='', editable=False, max_length=32),
        ),
    ]