# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20171030_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 246128), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 244128), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 245128), verbose_name='添加时间'),
        ),
    ]