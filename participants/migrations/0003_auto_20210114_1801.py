# Generated by Django 3.1.5 on 2021-01-14 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0002_participant_institusi_peserta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='foto_peserta',
            field=models.ImageField(upload_to='media/img/img_peserta'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='foto_rapor',
            field=models.ImageField(upload_to='media/img/img_rapor'),
        ),
    ]
