from django.db import models

# Create your models here.


class Event(models.Model):
    nama_event = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_start = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_event)


class JawabanTheaterModelSMP(models.Model):
    exam_code = models.CharField(max_length=255)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_peserta)


class JawabanTheaterModelSMA(models.Model):
    exam_code = models.CharField(max_length=255)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama_peserta)
