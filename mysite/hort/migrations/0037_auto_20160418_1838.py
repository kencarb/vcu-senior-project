# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-18 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0036_auto_20160418_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Status',
            field=models.CharField(blank=True, choices=[('OP', 'Open'), ('FF', 'Fullfilled')], max_length=10),
        ),
    ]
