# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-12 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boxapp', '0011_auto_20171112_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('order_amount', models.CharField(max_length=20)),
            ],
        ),
    ]
