# Generated by Django 4.1.2 on 2022-11-19 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
