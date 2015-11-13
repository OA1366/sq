# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=60)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Title', models.CharField(max_length=100)),
                ('Publisher', models.CharField(max_length=40)),
                ('PublishDate', models.DateField(null=True, blank=True)),
                ('Price', models.CharField(max_length=60)),
                ('AuthorID', models.ForeignKey(to='books.Author')),
            ],
        ),
    ]
