# Generated by Django 4.2.15 on 2024-08-22 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_players_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='vr_pirate_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\\pirate')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vr_pistol_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\\pistol')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vr_racer_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\racer')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vr_roller_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\roller')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vr_ultimechs_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\\ultimechs')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='vr_zombie_Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Roll_number', models.CharField(max_length=15, null=True)),
                ('Branch', models.CharField(max_length=20)),
                ('Year', models.CharField(max_length=15)),
                ('Email_id', models.EmailField(max_length=254, null=True)),
                ('Phone', models.IntegerField(null=True)),
                ('DOB', models.DateField(null=True)),
                ('Score', models.IntegerField(null=True)),
                ('Avatar', models.ImageField(blank=True, null=True, upload_to='D:\\websocket\\ET\\ETweb\\media\\zombie')),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Players',
        ),
    ]