# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.postgres.fields import JSONField
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20150224_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='data',
            field=JSONField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
