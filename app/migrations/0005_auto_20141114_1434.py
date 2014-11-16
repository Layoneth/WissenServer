# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20141023_1108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categorías', 'verbose_name': 'categoría'},
        ),
        migrations.AlterModelOptions(
            name='categorytranslate',
            options={'verbose_name_plural': 'traducciones de las categorías', 'verbose_name': 'traducción de las categorías'},
        ),
        migrations.AlterModelOptions(
            name='discipline',
            options={'verbose_name': 'disciplina'},
        ),
        migrations.AlterModelOptions(
            name='disciplinetranslate',
            options={'verbose_name_plural': 'traducciones de las disciplinas', 'verbose_name': 'traducción de una disciplina'},
        ),
        migrations.AlterModelOptions(
            name='entity',
            options={'verbose_name_plural': 'entidades', 'verbose_name': 'entidad'},
        ),
        migrations.AlterModelOptions(
            name='level',
            options={'verbose_name_plural': 'niveles', 'verbose_name': 'nivel'},
        ),
        migrations.AlterModelOptions(
            name='leveltranslate',
            options={'verbose_name_plural': 'traducciones de los niveles', 'verbose_name': 'traducción de los niveles'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name_plural': 'mensajes privados', 'verbose_name': 'mensaje privado'},
        ),
        migrations.AlterField(
            model_name='message',
            name='user_to',
            field=models.ForeignKey(related_name='receptor', to=settings.AUTH_USER_MODEL),
        ),
    ]
