# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myBillWeb_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='checksum',
            field=models.CharField(default=datetime.datetime(2015, 2, 11, 20, 49, 23, 457086, tzinfo=utc), max_length=200, verbose_name='Checksum'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='checksum',
            field=models.CharField(default=datetime.datetime(2015, 2, 11, 20, 49, 30, 177238, tzinfo=utc), max_length=200, verbose_name='Checksum'),
            preserve_default=False,
        ),
    ]
