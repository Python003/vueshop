# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 15:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 23, 49, 42, 305631), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userfav',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 23, 49, 42, 302631), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='userleavingmessage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 30, 23, 49, 42, 304631), verbose_name='添加时间'),
        ),
    ]
