# Generated by Django 3.1.4 on 2021-01-02 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0016_fastsoal'),
    ]

    operations = [
        migrations.CreateModel(
            name='JawabanFast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_soal', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('id_peserta', models.CharField(max_length=255)),
                ('exam_code', models.CharField(max_length=255)),
                ('jawaban_peserta', models.CharField(max_length=255)),
            ],
        ),
    ]