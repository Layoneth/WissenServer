# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_with_pay'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name_plural': 'respuestas', 'verbose_name': 'respuesta'},
        ),
        migrations.AlterModelOptions(
            name='bug',
            options={'verbose_name_plural': 'bugs del sistema', 'verbose_name': 'bug'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name_plural': 'eventos', 'verbose_name': 'evento'},
        ),
        migrations.AlterModelOptions(
            name='inscription',
            options={'verbose_name_plural': 'inscripciones', 'verbose_name': 'inscripción'},
        ),
        migrations.AlterModelOptions(
            name='participant_level',
            options={'verbose_name_plural': 'asignaciones de niveles a participantes', 'verbose_name': 'asignación de nivel a participante'},
        ),
        migrations.AlterModelOptions(
            name='test',
            options={'verbose_name_plural': 'test(exámenes respondidos)', 'verbose_name': 'test'},
        ),
        migrations.AlterModelOptions(
            name='user_event',
            options={'verbose_name_plural': 'asignaciones de eventos a usuarios', 'verbose_name': 'Asignación de evento a usuario'},
        ),
    ]
