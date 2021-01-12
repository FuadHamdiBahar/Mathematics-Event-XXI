# Generated by Django 3.1.4 on 2020-12-29 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0002_participant_exam_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='email_peserta',
            field=models.EmailField(default='email@email.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='participant',
            name='jenis_kelamin',
            field=models.CharField(choices=[('L', 'Laki-Laki'), ('P', 'Perempuan')], default='L', max_length=30),
            preserve_default=False,
        ),
    ]