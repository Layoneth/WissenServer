# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
        ('event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20141023_1108'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='exam',
            field=models.ForeignKey(to='exam.Exam'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='inscripcion',
            field=models.ForeignKey(to='event.Inscription'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant_level',
            name='nivel',
            field=models.ForeignKey(to='app.Level'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='participant_level',
            name='user',
            field=models.ForeignKey(related_name='participant_levels', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscription',
            name='categoria',
            field=models.ForeignKey(to='app.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscription',
            name='signed_by',
            field=models.ForeignKey(related_name='inscription_signed_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inscription',
            name='user',
            field=models.ForeignKey(related_name='inscriptions', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bug',
            name='fixed_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bug',
            name='reported_by',
            field=models.ForeignKey(related_name='bug_reported_by', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='preg',
            field=models.ForeignKey(to='exam.Question'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='test',
            field=models.ForeignKey(to='event.Test'),
            preserve_default=True,
        ),
    ]
