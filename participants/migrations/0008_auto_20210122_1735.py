# Generated by Django 3.1.5 on 2021-01-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0007_auto_20210119_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='paket_soal',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
    ]