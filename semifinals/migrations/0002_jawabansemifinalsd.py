# Generated by Django 3.1.5 on 2021-02-03 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('semifinals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JawabanSemifinalSD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=255)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('exam_code', models.CharField(max_length=255)),
                ('paket_soal', models.CharField(max_length=10)),
                ('jawaban_peserta', models.CharField(max_length=255)),
                ('submit_time', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]