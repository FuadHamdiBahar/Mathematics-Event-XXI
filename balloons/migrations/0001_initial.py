# Generated by Django 3.1.5 on 2021-02-03 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalloonSoalModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soal_acak', models.CharField(max_length=10)),
                ('foto_soal', models.ImageField(upload_to='img/img_soal')),
                ('exam_code', models.CharField(blank=True, max_length=255)),
                ('nama_peserta', models.CharField(blank=True, max_length=255)),
                ('is_taken', models.BooleanField(default=False)),
            ],
        ),
    ]
