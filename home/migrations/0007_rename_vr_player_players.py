# Generated by Django 4.2.15 on 2024-08-18 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_rename_avatar_vr_player_avatar'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='vr_player',
            new_name='Players',
        ),
    ]
