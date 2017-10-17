# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 03:47
from __future__ import unicode_literals

import coffeehouse.about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.CharField(max_length=1000, validators=[coffeehouse.about.models.validate_comment_word_count])),
            ],
        ),
    ]