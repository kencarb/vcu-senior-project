# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-24 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0022_auto_20160323_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='BackOrderDetailID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='Ledger',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='OrigDetailID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='ScheduledCompleteDT',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='ScheduledStartDT',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
