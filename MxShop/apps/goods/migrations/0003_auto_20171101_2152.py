# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 13:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20171030_2349'),
    ]

    operations = [
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
        migrations.AddField(
            model_name='goodscategorybrand',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 235127), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 232127), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 229127), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 230127), verbose_name='添加时间'),
        ),
        migrations.AlterField(
            model_name='goodsimage',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 1, 21, 52, 10, 234127), verbose_name='添加时间'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目'),
        ),
        migrations.AddField(
            model_name='indexad',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods'),
        ),
    ]
