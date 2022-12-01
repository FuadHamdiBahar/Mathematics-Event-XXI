from django.db import models

# Create your models here.


class Event(models.Model):
    nama_event = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_start = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_event)


class SoalFastModel(models.Model):
    foto_soal = models.ImageField(upload_to='img/img_soal')


class JawabanFastModel(models.Model):
    id_peserta = models.CharField(max_length=255)
    nama_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    paket_soal = models.CharField(max_length=10)
    jawaban_peserta = models.CharField(max_length=255)
    result_peserta = models.IntegerField(blank=True, null=True)
    jawaban_benar = models.PositiveIntegerField(blank=True, null=True)
    jawaban_salah = models.PositiveIntegerField(blank=True, null=True)
    jawaban_kosong = models.PositiveIntegerField(blank=True, null=True)
    submit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.id_peserta, self.nama_peserta)
