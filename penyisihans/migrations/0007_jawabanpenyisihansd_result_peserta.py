# Generated by Django 3.1.5 on 2021-02-03 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('penyisihans', '0006_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='jawabanpenyisihansd',
            name='result_peserta',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
