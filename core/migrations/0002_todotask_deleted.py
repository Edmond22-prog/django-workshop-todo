# Generated by Django 4.2.7 on 2023-11-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todotask',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]