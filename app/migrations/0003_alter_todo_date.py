# Generated by Django 3.2 on 2021-04-11 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
