# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 12:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20170405_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='caiq_score',
            field=models.FloatField(default=0),
        ),
    ]
