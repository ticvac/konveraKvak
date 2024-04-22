# Generated by Django 5.0.4 on 2024-04-22 14:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='StouplNaSamce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playerId', models.IntegerField()),
                ('gameId', models.IntegerField()),
                ('color', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isFliped', models.BooleanField(default=False)),
                ('type', models.IntegerField(choices=[(1, 'LEKNIN'), (2, 'KOMAR'), (3, 'BAHNO'), (4, 'STIKA'), (5, 'RAKOS'), (60, 'MORDY_SAMEC'), (61, 'FIALOVY_SAMEC'), (62, 'CERVENY_SAMEC'), (63, 'RUZOVY_SAMEC'), (64, 'ZELENY_SAMEC'), (65, 'ZLUTY_SAMEC')])),
                ('backgroundType', models.IntegerField(choices=[(1, 'BEZ_STIKY'), (2, 'STIKA_DOLE'), (3, 'STIKA_NAHORE')])),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Žába',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isQueen', models.BooleanField(default=False)),
                ('tileId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstOnMove', models.BooleanField(default=True)),
                ('moveCount', models.IntegerField(default=0)),
                ('boardId', models.IntegerField()),
                ('isOver', models.BooleanField(default=False)),
                ('player1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player1_reverse', to='kvak.player')),
                ('player2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player2_reverse', to='kvak.player')),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiles', models.ManyToManyField(to='kvak.tile')),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='zaby',
            field=models.ManyToManyField(to='kvak.žába'),
        ),
    ]