# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20170414_1157'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_code',
            field=models.CharField(default=0, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=300),
        ),
    ]