# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
        ('i18n', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20141023_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('descripcion', models.CharField(blank=True, max_length=200, null=True)),
                ('dirigido', models.BooleanField(default=False)),
                ('duracion_preg', models.IntegerField(blank=True, max_length=3, null=True)),
                ('duracion_exam', models.IntegerField(blank=True, max_length=3, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
                ('categoria_id', models.ForeignKey(to='app.Category')),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('evento_id', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exam_Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('added_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('exam', models.ForeignKey(to='exam.Exam')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pregunta', models.TextField(blank=True, verbose_name='Exam', null=True)),
                ('duracion', models.IntegerField(blank=True, max_length=3, null=True)),
                ('correct', models.IntegerField(max_length=1)),
                ('aleatorio', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(to='event.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question_Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
                ('assigned_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categoria', models.ForeignKey(to='app.Category')),
                ('preg', models.ForeignKey(to='exam.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='QuestionTranslate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('enunciado', models.TextField(blank=True, verbose_name='Exam', null=True)),
                ('img', models.FileField(blank=True, max_length=400, upload_to='images/questions', null=True)),
                ('opc1', models.TextField(blank=True, null=True)),
                ('opc2', models.TextField(blank=True, null=True)),
                ('opc3', models.TextField(blank=True, null=True)),
                ('opc4', models.TextField(blank=True, null=True)),
                ('img1', models.FileField(blank=True, max_length=400, upload_to='images/questions', null=True)),
                ('img2', models.FileField(blank=True, max_length=400, upload_to='images/questions', null=True)),
                ('img3', models.FileField(blank=True, max_length=400, upload_to='images/questions', null=True)),
                ('img4', models.FileField(blank=True, max_length=400, upload_to='images/questions', null=True)),
                ('translated', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('udpated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('idioma', models.ForeignKey(to='i18n.Language')),
                ('preg', models.ForeignKey(to='exam.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='exam_question',
            name='preg',
            field=models.ForeignKey(to='exam.Question'),
            preserve_default=True,
        ),
    ]
