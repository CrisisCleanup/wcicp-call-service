# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-09 00:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calls', '0017_AdditionalModelUpdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calls.Language'),
        ),
        migrations.AlterField(
            model_name='caller',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='caller',
            name='preferred_language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='calls.Language'),
        ),
        migrations.AlterField(
            model_name='caller',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='queue_duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='connectfirstevent',
            name='sess_duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
