# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0024_auto_20160327_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='EnteredBy',
            field=models.IntegerField(choices=[(2, 'admin'), (4, 'crew'), (5, 'cust'), (1, 'ken'), (3, 'mgr')]),
        ),
        migrations.AlterField(
            model_name='orders',
            name='StatusBy',
            field=models.IntegerField(blank=True, choices=[(2, 'admin'), (4, 'crew'), (5, 'cust'), (1, 'ken'), (3, 'mgr')]),
        ),
    ]
