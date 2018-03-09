# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 22:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0013_auto_20160313_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodandservices',
            name='LedgerIn',
            field=models.IntegerField(choices=[(1000, 1000), (1005, 1005), (1010, 1010), (1020, 1020), (1030, 1030), (1040, 1040), (1050, 1050), (1060, 1060), (1070, 1070), (2000, 2000), (2020, 2020), (2030, 2030), (3000, 3000), (3999, 3999), (4000, 4000), (4005, 4005), (4010, 4010), (4020, 4020), (4025, 4025), (4071, 4071), (5000, 5000), (5003, 5003), (5005, 5005), (5010, 5010), (5020, 5020), (5025, 5025), (5030, 5030), (5040, 5040), (5050, 5050), (5060, 5060), (5061, 5061), (5062, 5062), (5065, 5065), (5067, 5067), (5070, 5070), (5071, 5071), (5080, 5080), (5085, 5085)], default=0),
        ),
    ]