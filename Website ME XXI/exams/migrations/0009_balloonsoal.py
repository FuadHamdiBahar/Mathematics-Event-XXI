# Generated by Django 3.1.4 on 2020-12-28 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0008_jawaban_exam_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='BalloonSoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_soal', models.ImageField(upload_to='static/assets/img/img_soal')),
                ('soal_acak', models.CharField(max_length=50)),
                ('jawaban_benar', models.TextField()),
            ],
        ),
    ]