# Generated by Django 3.2.8 on 2021-11-03 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0012_auto_20210410_1032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='participant',
            old_name='playoff',
            new_name='playoff_balloon',
        ),
        migrations.AddField(
            model_name='participant',
            name='playoff_fast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='playoff_penyisihan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='playoff_semifinal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='playoff_theatre',
            field=models.BooleanField(default=False),
        ),
    ]