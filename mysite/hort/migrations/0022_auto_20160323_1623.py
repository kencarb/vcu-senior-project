# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-23 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0021_auto_20160323_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='Type',
            field=models.CharField(choices=[('P', 'Purchase'), ('S', 'Sale')], max_length=10),
        ),
    ]
