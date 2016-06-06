# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-06 21:15
from __future__ import unicode_literals

from decimal import Decimal
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0007_auto_20160603_2153'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.IntegerField()),
                ('name', models.CharField(blank=True, default='', max_length=255)),
                ('url', models.URLField(blank=True, default='', max_length=2048)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=8)),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stores.Store')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='offer',
            unique_together=set([('store', 'external_id')]),
        ),
    ]
