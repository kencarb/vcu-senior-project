# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0038_auto_20160425_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='OrderID',
            field=models.IntegerField(),
        ),
    ]