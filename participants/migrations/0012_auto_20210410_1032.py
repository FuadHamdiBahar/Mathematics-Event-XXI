# Generated by Django 3.1.5 on 2021-04-10 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0011_auto_20210325_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='playoff_balloon',
            new_name='playoff',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='playoff_fast',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='playoff_penyisihan',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='playoff_semifinal',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='playoff_theatre',
        ),
    ]