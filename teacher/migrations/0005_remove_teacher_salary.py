# Generated by Django 3.0.5 on 2021-12-15 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20211214_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='salary',
        ),
    ]
