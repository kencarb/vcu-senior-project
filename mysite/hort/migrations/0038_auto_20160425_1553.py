# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-25 19:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0037_auto_20160418_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='OrderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hort.Orders'),
        ),
    ]
