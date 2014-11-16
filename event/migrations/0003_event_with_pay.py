# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20141023_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='with_pay',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
