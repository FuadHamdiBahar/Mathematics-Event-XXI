# Generated by Django 3.1.5 on 2021-01-14 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('institutions', '0001_initial'),
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='institusi_peserta',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='institutions.institution'),
            preserve_default=False,
        ),
    ]
