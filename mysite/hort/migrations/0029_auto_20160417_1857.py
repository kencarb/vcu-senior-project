# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-17 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0028_auto_20160328_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='OrderID',
            field=models.IntegerField(),
        ),
    ]
