# Generated by Django 4.2.3 on 2024-07-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chats',
            name='combineroom',
            field=models.BooleanField(default=False),
        ),
    ]
