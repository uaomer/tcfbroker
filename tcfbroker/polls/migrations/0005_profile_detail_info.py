# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170405_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='detail_info',
            field=models.TextField(default=''),
        ),
    ]
