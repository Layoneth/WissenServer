# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('i18n', '0003_auto_20141113_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name_plural': 'idiomas', 'verbose_name': 'idioma'},
        ),
        migrations.AlterModelOptions(
            name='languagesregistered',
            options={'verbose_name_plural': 'idiomas registrados', 'verbose_name': 'idioma registrado'},
        ),
    ]
