# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0012_auto_20170306_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='member_Name',
            field=models.CharField(editable=False, max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='memberid',
            field=models.IntegerField(editable=False, null=True),
        ),
    ]
