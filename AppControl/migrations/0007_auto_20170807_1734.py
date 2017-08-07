# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 10:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boxapp', '0009_auto_20170727_0225'),
        ('AppControl', '0006_auto_20170804_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('temp', models.FloatField(default=0.0)),
                ('humi', models.FloatField(default=0.0)),
            ],
        ),
        migrations.DeleteModel(
            name='Box',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='box2',
            name='code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxapp.Box'),
        ),
    ]