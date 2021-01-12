from participants.models import Participant
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Soal(models.Model):
    foto_soal = models.ImageField(upload_to='static/assets/img/img_soal')
    jawaban_A = models.CharField(max_length=100)
    jawaban_B = models.CharField(max_length=100)
    jawaban_C = models.CharField(max_length=100)
    jawaban_D = models.CharField(max_length=100)
    jawaban_E = models.CharField(max_length=100)
    pilihan_jawaban = (
        ('A', jawaban_A),
        ('B', jawaban_B),
        ('C', jawaban_C),
        ('D', jawaban_D),
        ('E', jawaban_E),
    )
    jawaban_benar = models.CharField(max_length=100, choices=pilihan_jawaban)

    kategori_soal = (
        ('Penyisihan', 'Penyisihan'),
        ('Semifinal', 'Semifinal'),
        ('Fastgame', 'Fastgame'),
        ('Balloongame', 'Balloongame'),
    )
    kategori = models.CharField(max_length=50, choices=kategori_soal)

    tingkat_pendidikan = (
        ('SD', 'Sekolah Dasar'),
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
    )
    tingkat = models.CharField(max_length=10, choices=tingkat_pendidikan)

    def __str__(self):
        return "{}. {}".format(self.id, self.jawaban_benar)


class BalloonSoal(models.Model):
    foto_soal = models.ImageField(
        upload_to='static/assets/img/img_soal', blank=True)
    soal_acak = models.CharField(max_length=50)
    exam_code = models.CharField(max_length=255)
    is_taken = models.BooleanField(default=False)
    jawaban_benar = models.TextField(blank=True)

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.soal_acak, self.is_taken)


class FastSoal(models.Model):
    foto_soal = models.ImageField(
        upload_to='static/assets/img/img_soal', blank=True)

    def __str__(self):
        return '{}. {}'.format(self.id, self.foto_soal)


class Jawaban(models.Model):
    nama_peserta = models.CharField(max_length=255)
    id_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    tingkat = models.CharField(max_length=255)
    jawaban_peserta = models.CharField(max_length=255)
    result = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}. {}'.format(self.id_peserta, self.nama_peserta)


class JawabanSemiFinal(models.Model):
    nama_peserta = models.CharField(max_length=255)
    id_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    jawaban_peserta = models.CharField(max_length=255)
    result = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '{}. {}'.format(self.id_peserta, self.nama_peserta)


class JawabanBalloon(models.Model):
    nama_peserta = models.CharField(max_length=255)
    id_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    soal_peserta = models.CharField(max_length=50)
    jawaban_peserta = models.CharField(max_length=255)

    def __str__(self):
        return '{}. {}'.format(self.nama_peserta, self.soal_peserta)


class JawabanFast(models.Model):
    id_soal = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    id_peserta = models.CharField(max_length=255)
    exam_code = models.CharField(max_length=255)
    jawaban_peserta = models.CharField(max_length=255)

    def __str__(self):
        return '{} soal {}'.format(self.nama_peserta, self.id_soal)
