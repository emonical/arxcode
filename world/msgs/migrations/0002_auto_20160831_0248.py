# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-31 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("msgs", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="inform",
            table="comms_inform",
        ),
    ]
