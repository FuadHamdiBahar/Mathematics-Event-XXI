from django.db import models

# Create your models here.


class Event(models.Model):
    nama_event = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_start = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_event)


class BalloonSoalModel(models.Model):
    soal_acak = models.CharField(max_length=10)
    foto_soal = models.ImageField(upload_to='img/img_soal')

    # peserta
    exam_code = models.CharField(max_length=255, blank=True)
    nama_peserta = models.CharField(max_length=255, blank=True)

    is_taken = models.BooleanField(default=False)

    # jawaban
    jawaban = models.CharField(max_length=255, blank=True)
    submit_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.soal_acak)
