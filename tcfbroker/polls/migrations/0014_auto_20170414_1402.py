# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 09:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20170414_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='q_app',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='q_comp',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='q_data',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='q_net',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='q_phy',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='question',
            name='q_sto',
            field=models.CharField(default=0, max_length=10),
        ),
    ]
