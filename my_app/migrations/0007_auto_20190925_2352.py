# Generated by Django 2.2.5 on 2019-09-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0006_todo_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='true',
            field=models.BooleanField(default='False'),
        ),
    ]
