# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hardware',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hdName', models.CharField(max_length=32, verbose_name=b'Hardware Name')),
                ('hdCode', models.CharField(max_length=32, verbose_name=b'Hardware Code')),
                ('hdDesc', models.TextField(null=True, verbose_name=b'Hardware Description', blank=True)),
                ('hdType', models.CharField(max_length=16, verbose_name=b'Hardware Type')),
            ],
        ),
    ]
