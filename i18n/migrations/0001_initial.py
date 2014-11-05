# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('codigo', models.CharField(max_length=5)),
                ('codigo2', models.CharField(blank=True, max_length=200, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('original', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LanguagesRegistered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('es_principal', models.BooleanField(default=False)),
                ('event', models.ForeignKey(to='event.Event')),
                ('idioma', models.ForeignKey(to='i18n.Language')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
