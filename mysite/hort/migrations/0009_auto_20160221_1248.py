# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0008_auto_20160221_0101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='AccountingDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='CheckedOutToFillBy',
            field=models.IntegerField(blank=True, choices=[(2, 'admin'), (4, 'crew'), (5, 'cust'), (1, 'ken'), (3, 'mgr')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='CheckedOutToFillDT',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='DataEntryCompleteBy',
            field=models.IntegerField(blank=True, choices=[(2, 'admin'), (4, 'crew'), (5, 'cust'), (1, 'ken'), (3, 'mgr')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='DataEntryCompleteDT',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='InOrOut',
            field=models.IntegerField(blank=True, choices=[(1, 'In'), (-1, 'Out')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='InitialStatus',
            field=models.CharField(choices=[('OP', 'Open'), ('FF', 'Fullfilled'), ('CA', 'Cancelled'), ('SH', 'Shipped')], max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='PONumber',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='QueuedForPSX12DT',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='SentViaPXS12DT',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Status',
            field=models.CharField(blank=True, choices=[('OP', 'Open'), ('FF', 'Fullfilled'), ('CA', 'Cancelled'), ('SH', 'Shipped')], max_length=10),
        ),
        migrations.AlterField(
            model_name='orders',
            name='StatusBy',
            field=models.IntegerField(blank=True, choices=[(2, 'admin'), (4, 'crew'), (5, 'cust'), (1, 'ken'), (3, 'mgr')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='StatusHistory',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='orders',
            name='Type',
            field=models.CharField(choices=[('A', 'yadda'), ('B', 'babba')], max_length=10),
        ),
    ]