# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_users_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallets',
            name='wal_balance',
            field=models.IntegerField(default=0),
        ),
    ]