# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20170306_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='member_Name',
            field=models.CharField(default=b'Nill', editable=False, max_length=140, null=True),
        ),
    ]
