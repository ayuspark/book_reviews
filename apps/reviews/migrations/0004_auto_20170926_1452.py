# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20170926_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='author',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
    ]