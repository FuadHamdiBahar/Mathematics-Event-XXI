# Generated by Django 3.1.5 on 2021-03-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balloons', '0007_balloonsoalmodel_submit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balloonsoalmodel',
            name='submit_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
