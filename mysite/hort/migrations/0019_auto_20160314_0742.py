# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-14 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0018_auto_20160314_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodandservices',
            name='Class',
            field=models.CharField(choices=[('Good', 'Good'), ('Svcs', 'Svcs'), ('Acct', 'Acct')], max_length=12),
        ),
    ]