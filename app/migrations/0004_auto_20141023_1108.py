# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('i18n', '0001_initial'),
        ('app', '0003_category_categorytranslate_disciplinetranslate_level_leveltranslate_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='leveltranslate',
            name='idioma',
            field=models.ForeignKey(to='i18n.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leveltranslate',
            name='level',
            field=models.ForeignKey(related_name='traducciones', to='app.Level'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='level',
            name='event',
            field=models.ForeignKey(to='event.Event', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinetranslate',
            name='discipline',
            field=models.ForeignKey(related_name='traducciones', to='app.Discipline'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='disciplinetranslate',
            name='idioma',
            field=models.ForeignKey(to='i18n.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categorytranslate',
            name='category',
            field=models.ForeignKey(related_name='traducciones', to='app.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='categorytranslate',
            name='idioma',
            field=models.ForeignKey(to='i18n.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='discipline',
            field=models.ForeignKey(to='app.Discipline'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='event',
            field=models.ForeignKey(to='event.Event', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.ForeignKey(to='app.Level'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='discipline',
            name='event',
            field=models.ForeignKey(to='event.Event', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entity',
            name='event',
            field=models.ForeignKey(to='event.Event', blank=True, null=True),
            preserve_default=True,
        ),
    ]
