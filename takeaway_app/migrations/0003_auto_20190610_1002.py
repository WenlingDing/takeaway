# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-10 10:02
from __future__ import unicode_literals

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('takeaway_app', '0002_delete_slide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='image',
        ),
        migrations.AddField(
            model_name='food',
            name='photo',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]
