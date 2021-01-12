from django.db import models

# Create your models here.


class Institution(models.Model):
    nama_sekolah = models.CharField(max_length=255)
    provinsi_sekolah = models.CharField(max_length=255)
    kabupaten_sekolah = models.CharField(max_length=255)
    kecamatan_sekolah = models.CharField(max_length=255)
    alamat_sekolah = models.CharField(max_length=255)
    email_sekolah = models.CharField(max_length=255, blank=True)
    kontak_guru_pendamping = models.CharField(max_length=255, blank=True)
    kontak_sekolah = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return "{}".format(self.nama_sekolah)
