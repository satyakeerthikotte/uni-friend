# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 01:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_recommendation', '0002_auto_20170425_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobs',
            name='Jobtitle',
        ),
        migrations.AddField(
            model_name='jobs',
            name='description2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='jobtitle',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='jobs',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='company',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='description',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
