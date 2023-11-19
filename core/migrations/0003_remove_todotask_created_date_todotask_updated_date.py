# Generated by Django 4.2.7 on 2023-11-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_todotask_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotask',
            name='created_date',
        ),
        migrations.AddField(
            model_name='todotask',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
