from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.

from institutions.models import Institution


class Participant(User):
    no_id = models.CharField(max_length=255, blank=True)
    nis_peserta = models.CharField(max_length=255)

    kelamin = (('Laki-laki', 'Laki-Laki'), ('Perempuan', 'Perempuan'))
    jenis_kelamin = models.CharField(max_length=30, choices=kelamin)
    institusi_peserta = models.ForeignKey(Institution, on_delete=CASCADE)

    tingkat_pendidikan = (
        ('SD', 'Sekolah Dasar'),
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
    )
    tingkat = models.CharField(max_length=10, choices=tingkat_pendidikan)
    kontak_peserta = models.CharField(max_length=255, blank=True)
    email_peserta = models.EmailField()
    foto_peserta = models.ImageField(upload_to='static/assets/img/img_peserta')
    foto_rapor = models.ImageField(
        upload_to='static/assets/img/img_kartu_pelajar')

    exam_code = models.CharField(max_length=255, blank=True)

    penyisihan = models.BooleanField(default=False)
    semifinal = models.BooleanField(default=False)
    fastgame = models.BooleanField(default=False)
    balloongame = models.BooleanField(default=False)
    theatregame = models.BooleanField(default=False)

    def __str__(self):
        return "{}. {}".format(self.id, self.first_name)
