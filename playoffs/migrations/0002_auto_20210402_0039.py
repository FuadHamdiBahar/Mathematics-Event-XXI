# Generated by Django 3.1.5 on 2021-04-01 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playoffs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayOffBalloon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('jawaban', models.CharField(max_length=255)),
                ('submit_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayOffFast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('jawaban', models.CharField(max_length=255)),
                ('submit_time', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PlayOffPenyisihan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('jawaban', models.CharField(max_length=255)),
                ('submit_time', models.DateTimeField(auto_now=True)),
                ('tingkat', models.CharField(choices=[('SD', 'Sekolah Dasar'), ('SMP', 'Sekolah Menengah Pertama'), ('SMA', 'Sekolah Menengah Atas')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayOffSemifinal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('jawaban', models.CharField(max_length=255)),
                ('submit_time', models.DateField(auto_now=True)),
                ('tingkat', models.CharField(choices=[('SD', 'Sekolah Dasar'), ('SMP', 'Sekolah Menengah Pertama'), ('SMA', 'Sekolah Menengah Atas')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='PlayOffTheatre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_peserta', models.CharField(max_length=50)),
                ('nama_peserta', models.CharField(max_length=255)),
                ('jawaban', models.CharField(max_length=255)),
                ('submit_time', models.DateField(auto_now=True)),
                ('tingkat', models.CharField(choices=[('SMP', 'Sekolah Menengah Pertama'), ('SMA', 'Sekolah Menengah Atas')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SoalPlayoff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
                ('foto_soal', models.ImageField(upload_to='')),
                ('babak', models.CharField(choices=[('penyisihan', 'Penyisihan'), ('semifinal', 'Semifinal'), ('fast', 'Fast'), ('balloon', 'Balloon'), ('thatre', 'Theatre')], max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='PlayOffPenyisihanSD',
        ),
    ]
