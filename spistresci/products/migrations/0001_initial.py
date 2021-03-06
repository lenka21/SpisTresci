# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title of Product')),
                ('external_id', models.IntegerField()),
                ('url', models.URLField(default='', max_length=2048)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
        ),
    ]
