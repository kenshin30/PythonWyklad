# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instruktorzy', '0002_instruktor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instruktor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='instruktorzy/'),
        ),
    ]
