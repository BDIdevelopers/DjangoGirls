# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-02 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_contributor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
