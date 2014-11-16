# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'verbose_name_plural': 'examenes', 'verbose_name': 'examen'},
        ),
        migrations.AlterModelOptions(
            name='exam_question',
            options={'verbose_name_plural': 'asignaciones de preguntas a exámenes', 'verbose_name': 'asignación de pregunta a exámenes'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name_plural': 'preguntas', 'verbose_name': 'pregunta'},
        ),
        migrations.AlterModelOptions(
            name='question_category',
            options={'verbose_name_plural': 'asignaciones de preguntas a categorías', 'verbose_name': 'asignación de pregunta a categoría'},
        ),
        migrations.AlterModelOptions(
            name='questiontranslate',
            options={'verbose_name_plural': 'traducciones de las preguntas', 'verbose_name': 'traducción de una pregunta'},
        ),
    ]
