# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 16:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160716_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.TextField(max_length=150, verbose_name='Категория'),
        ),
    ]