# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20170926_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=140),
        ),
    ]
