# Generated by Django 2.1.3 on 2018-12-17 09:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obec', '0004_auto_20181216_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='datum_pridani',
            field=models.DateField(default=datetime.date(2018, 12, 17)),
        ),
        migrations.AlterField(
            model_name='foto',
            name='datum',
            field=models.DateField(default=datetime.date(2018, 12, 17)),
        ),
        migrations.AlterField(
            model_name='foto',
            name='sirka',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
