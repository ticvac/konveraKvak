# Generated by Django 4.2.4 on 2024-04-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='žába',
            name='can_move',
            field=models.BooleanField(default=True),
        ),
    ]
