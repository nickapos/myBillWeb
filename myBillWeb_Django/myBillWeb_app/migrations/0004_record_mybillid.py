# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBillWeb_app', '0003_record_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='mybillId',
            field=models.IntegerField(default=-1, verbose_name='myBillDesktopId'),
            preserve_default=True,
        ),
    ]
