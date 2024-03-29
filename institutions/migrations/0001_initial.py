# Generated by Django 3.1.5 on 2021-01-14 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sekolah', models.CharField(max_length=255)),
                ('provinsi_sekolah', models.CharField(max_length=255)),
                ('kabupaten_sekolah', models.CharField(max_length=255)),
                ('kecamatan_sekolah', models.CharField(max_length=255)),
                ('alamat_sekolah', models.CharField(max_length=255)),
                ('email_sekolah', models.CharField(blank=True, max_length=255)),
                ('kontak_guru_pendamping', models.CharField(blank=True, max_length=255)),
                ('kontak_sekolah', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
