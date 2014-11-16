# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('i18n', '0002_auto_20141023_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagesregistered',
            name='event',
            field=models.ForeignKey(to='event.Event', related_name='languages'),
        ),
        migrations.AlterField(
            model_name='languagesregistered',
            name='idioma',
            field=models.ForeignKey(to='i18n.Language', related_name='registradas'),
        ),
    ]
