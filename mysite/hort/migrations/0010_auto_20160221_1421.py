# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0009_auto_20160221_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='AccountingDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='CheckedOutToFillDT',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='DataEntryCompleteDT',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='QueuedForPSX12DT',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='SentViaPXS12DT',
            field=models.DateTimeField(null=True),
        ),
    ]