# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 18:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='num_of_course',
            new_name='number_of_course',
        ),
    ]
