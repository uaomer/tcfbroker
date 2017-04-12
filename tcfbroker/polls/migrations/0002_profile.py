# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=200)),
                ('endpoint', models.CharField(max_length=200)),
                ('meta_text', models.CharField(max_length=200)),
                ('caiq_score', models.FloatField(default=0, max_length=10)),
            ],
        ),
    ]