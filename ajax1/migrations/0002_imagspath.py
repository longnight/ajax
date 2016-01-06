# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import ajax1.models


class Migration(migrations.Migration):

    dependencies = [
        ('ajax1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagsPath',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', sorl.thumbnail.fields.ImageField(upload_to=ajax1.models.user_upload_file)),
            ],
        ),
    ]
