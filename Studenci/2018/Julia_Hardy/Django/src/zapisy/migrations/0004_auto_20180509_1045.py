# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-09 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapisy', '0003_auto_20180509_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zapisy',
            name='your_choice',
            field=models.CharField(choices=[('1', 'Modern jazz'), ('2', 'Modern balet'), ('3', 'Afro dance'), ('4', 'Break dance')], max_length=1, null=True),
        ),
    ]
