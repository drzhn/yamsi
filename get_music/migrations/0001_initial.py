# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 21:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tokens',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=100)),
            ],
        ),
    ]
