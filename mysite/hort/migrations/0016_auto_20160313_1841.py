# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-13 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hort', '0015_auto_20160313_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodandservices',
            name='LedgerIn',
            field=models.IntegerField(choices=[(1000, '1000 Cash'), (1005, '1005 ACH'), (1010, '1010 Accounts Receivable'), (1020, '1020 Investments'), (1030, '1030 Inventory'), (1040, '1040 Equipment'), (1050, '1050 Vehicles'), (1060, '1060 Real Estate'), (1070, '1070 Furniture & Fixtures'), (2000, '2000 Trade Accounts Payable'), (2020, '2020 Current Loans'), (2030, '2030 Mortgages'), (3000, '3000 Paid in Capital'), (3999, '3999 Retained Earnings'), (4000, '4000 Sale of Goods'), (4005, '4005 Shipping Sales'), (4010, '4010 Sale of Services'), (4020, '4020 Food Contributions'), (4025, '4025 Cash Contributions'), (4071, '4071 Shipping'), (5000, '5000 Cost of Goods for Sale'), (5003, '5003 Dry Ice'), (5005, '5005 Postage & Shipping'), (5010, '5010 Cost of Services Sold'), (5020, '5020 Food Distributions'), (5025, '5025 Spoilage'), (5030, '5030 Wages'), (5040, '5040 Administrative Costs'), (5050, '5050 Office/Warehouse Rent'), (5060, '5060 Utilities'), (5061, '5061 Telephone'), (5062, '5062 Internet Access'), (5065, '5065 Gas, Oil, & Maintenance'), (5067, '5067 Vehicle Lease'), (5070, '5070 Postage'), (5071, '5071 Shipping'), (5080, '5080 Interest'), (5085, '5085 Inventory Shrinkage')], default=0),
        ),
        migrations.AlterField(
            model_name='goodandservices',
            name='LedgerOut',
            field=models.IntegerField(choices=[(1000, '1000 Cash'), (1005, '1005 ACH'), (1010, '1010 Accounts Receivable'), (1020, '1020 Investments'), (1030, '1030 Inventory'), (1040, '1040 Equipment'), (1050, '1050 Vehicles'), (1060, '1060 Real Estate'), (1070, '1070 Furniture & Fixtures'), (2000, '2000 Trade Accounts Payable'), (2020, '2020 Current Loans'), (2030, '2030 Mortgages'), (3000, '3000 Paid in Capital'), (3999, '3999 Retained Earnings'), (4000, '4000 Sale of Goods'), (4005, '4005 Shipping Sales'), (4010, '4010 Sale of Services'), (4020, '4020 Food Contributions'), (4025, '4025 Cash Contributions'), (4071, '4071 Shipping'), (5000, '5000 Cost of Goods for Sale'), (5003, '5003 Dry Ice'), (5005, '5005 Postage & Shipping'), (5010, '5010 Cost of Services Sold'), (5020, '5020 Food Distributions'), (5025, '5025 Spoilage'), (5030, '5030 Wages'), (5040, '5040 Administrative Costs'), (5050, '5050 Office/Warehouse Rent'), (5060, '5060 Utilities'), (5061, '5061 Telephone'), (5062, '5062 Internet Access'), (5065, '5065 Gas, Oil, & Maintenance'), (5067, '5067 Vehicle Lease'), (5070, '5070 Postage'), (5071, '5071 Shipping'), (5080, '5080 Interest'), (5085, '5085 Inventory Shrinkage')], default=0),
        ),
    ]
