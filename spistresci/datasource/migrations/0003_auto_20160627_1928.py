# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-27 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def migrate_fields(apps, schema_editor):
    XmlDataField = apps.get_model("datasource", "XmlDataField")
    DataSourceFieldName = apps.get_model("datasource", "DataSourceFieldName")

    # add required DSFNs
    for name in ['external_id', 'name', 'url', 'price']:
        DataSourceFieldName.objects.get_or_create(name=name)

    # migration
    xml_data_fields = XmlDataField.objects.all()

    for xml_data_field in xml_data_fields:
        dsfn, created = DataSourceFieldName.objects.get_or_create(name=xml_data_field.name)

        xml_data_field.datafield_name = dsfn
        xml_data_field.save()


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0002_auto_20160613_2248'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSourceFieldName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='xmldatafield',
            name='datafield_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='datasource.DataSourceFieldName'),
        ),
        migrations.RunPython(migrate_fields),
    ]