# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoryName', models.CharField(max_length=200, verbose_name='Category name')),
                ('add_date', models.DateField(verbose_name='date added')),
                ('comment', models.CharField(max_length=200, verbose_name='Comment')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyName', models.CharField(max_length=200, verbose_name='Company name')),
                ('add_date', models.DateField(verbose_name='date added')),
                ('comment', models.CharField(max_length=200, verbose_name='Comment')),
                ('category', models.ForeignKey(to='myBillWeb_app.Category')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('add_date', models.DateField(verbose_name='date added')),
                ('comment', models.CharField(max_length=200, verbose_name='Comment')),
                ('checksum', models.CharField(max_length=200, verbose_name='Checksum')),
                ('type_of_record', models.CharField(default=b'EX', max_length=2, choices=[(b'EX', b'Expenses'), (b'IN', b'Income')])),
                ('company', models.ForeignKey(to='myBillWeb_app.Company')),
                ('username', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('username', 'categoryName')]),
        ),
    ]
