# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustID', models.CharField(max_length=20)),
                ('FirstName', models.CharField(blank=True, max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('ExtraLine', models.CharField(blank=True, max_length=75)),
                ('StreetAddress', models.CharField(max_length=75)),
                ('PostOffice', models.CharField(max_length=50)),
                ('ZipCode', models.CharField(max_length=10)),
            ],
        ),
    ]
