# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myBillWeb_app', '0005_auto_20150211_2132'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='add_date',
        ),
        migrations.AddField(
            model_name='record',
            name='issue_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='issue date', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='record',
            name='pay_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='pay date', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='add_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='date added', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='company',
            name='add_date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='date added', blank=True),
            preserve_default=True,
        ),
    ]
