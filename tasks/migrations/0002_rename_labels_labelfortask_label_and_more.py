# Generated by Django 4.1.2 on 2022-11-24 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labelfortask',
            old_name='labels',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='labels',
            new_name='label',
        ),
    ]