# Generated by Django 3.1.4 on 2020-12-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='exam_code',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]