# Generated by Django 2.2.5 on 2019-11-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='new_f',
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.TextField(default=''),
        ),
    ]
