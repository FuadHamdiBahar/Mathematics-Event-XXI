# Generated by Django 3.1.5 on 2021-03-02 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('balloons', '0002_balloonsoalmodel_jawaban'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_event', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
    ]
