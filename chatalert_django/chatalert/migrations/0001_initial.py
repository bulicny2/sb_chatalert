# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.TextField(unique=True)),
                ('creation_datetime', models.DateTimeField(blank=True, null=True)),
                ('message_type', models.TextField(blank=True)),
                ('source', models.TextField(blank=True)),
                ('message_url', models.TextField(blank=True)),
                ('text', models.TextField(blank=True)),
                ('author', models.TextField(blank=True)),
                ('author_age', models.IntegerField(blank=True, null=True)),
                ('city_state', models.TextField(blank=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('phone_number', models.TextField(blank=True)),
                ('post_id', models.TextField(blank=True)),
                ('label_auto', models.IntegerField(choices=[(-1, b'No Label'), (0, b'Review'), (1, b'LE Interest'), (2, b'Urgent!')], default=-1)),
                ('label_user', models.IntegerField(choices=[(-1, b'No Label'), (0, b'Review'), (1, b'LE Interest'), (2, b'Urgent!')], default=-1)),
            ],
        ),
    ]
