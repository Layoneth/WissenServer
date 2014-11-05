# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('logo', models.CharField(null=True, blank=True, max_length=600)),
                ('direccion', models.CharField(null=True, blank=True, max_length=200)),
                ('dirigente', models.CharField(null=True, blank=True, max_length=200)),
                ('celular', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
