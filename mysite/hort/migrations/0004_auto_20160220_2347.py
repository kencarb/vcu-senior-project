# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0003_auto_20160220_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodandservices',
            name='PrimarySupplier',
            field=models.CharField(choices=[('W1234W', 'Weedy Wackers Inc.')], max_length=50),
        ),
    ]