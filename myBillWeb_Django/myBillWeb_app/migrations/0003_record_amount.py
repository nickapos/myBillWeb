# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBillWeb_app', '0002_auto_20150211_2049'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='amount',
            field=models.FloatField(default=0.0, verbose_name='Amount'),
            preserve_default=True,
        ),
    ]
