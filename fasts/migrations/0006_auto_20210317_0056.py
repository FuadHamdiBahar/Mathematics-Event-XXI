# Generated by Django 3.1.5 on 2021-03-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fasts', '0005_auto_20210317_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jawabanfastmodel',
            name='submit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]