# Generated by Django 4.1.2 on 2022-11-21 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0002_rename_date_joined_status_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]