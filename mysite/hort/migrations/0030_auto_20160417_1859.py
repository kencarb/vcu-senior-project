# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0029_auto_20160417_1857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='QtyInOrOut',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True),
        ),
    ]