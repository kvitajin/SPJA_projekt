# Generated by Django 2.1.3 on 2018-12-16 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obec', '0002_auto_20181216_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dokument',
            name='obrazek',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]