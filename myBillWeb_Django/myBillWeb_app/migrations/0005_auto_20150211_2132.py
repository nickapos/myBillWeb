# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBillWeb_app', '0004_record_mybillid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(default=b' ', max_length=200, null=True, verbose_name='Comment', blank=True),
            preserve_default=True,
        ),
    ]
