# Generated by Django 2.2.3 on 2019-08-10 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='formatter',
        ),
    ]
