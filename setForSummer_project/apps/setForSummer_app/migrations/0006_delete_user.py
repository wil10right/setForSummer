# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-29 01:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setForSummer_app', '0005_merge_20180629_0134'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]