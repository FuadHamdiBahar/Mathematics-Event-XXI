from django.db import models

# Create your model


class SoalPlayoff(models.Model):
    nama = models.CharField(max_length=50)
    foto_soal = models.ImageField()

    jenis_babak = (
        ('penyisihan', 'Penyisihan'),
        ('semifinal', 'Semifinal'),
        ('fast', 'Fast'),
        ('balloon', 'Balloon'),
        ('thatre', 'Theatre')
    )
    babak = models.CharField(max_length=20, choices=jenis_babak)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)


class PlayOffPenyisihan(models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateTimeField(auto_now=True)

    tingkat_pendidikan = (
        ('SD', 'Sekolah Dasar'),
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
    )
    tingkat = models.CharField(max_length=10, choices=tingkat_pendidikan)

    def __str__(self):
        return "{}. {}".format(self.id_peserta, self.nama_peserta)


class PlayOffSemifinal(models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateField(auto_now=True)

    tingkat_pendidikan = (
        ('SD', 'Sekolah Dasar'),
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
    )
    tingkat = models.CharField(max_length=10, choices=tingkat_pendidikan)

    def __str__(self):
        return "{}. {}".format(self.id_peserta, self.nama_peserta)


class PlayOffBalloon(models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.id_peserta, self.nama_peserta)


class PlayOffFast(models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.id_peserta, self.nama_peserta)


class PlayOffTheatre(models.Model):
    id_peserta = models.CharField(max_length=50)
    nama_peserta = models.CharField(max_length=255)
    jawaban = models.CharField(max_length=255)
    submit_time = models.DateField(auto_now=True)

    tingkat_pendidikan = (
        ('SMP', 'Sekolah Menengah Pertama'),
        ('SMA', 'Sekolah Menengah Atas'),
    )
    tingkat = models.CharField(max_length=10, choices=tingkat_pendidikan)

    def __str__(self):
        return "{}. {}".format(self.id_peserta, self.nama_peserta)
