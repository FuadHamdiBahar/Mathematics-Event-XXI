from datetime import datetime
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.

from participants.models import Participant
from .models import (
    Event, JawabanPenyisihanSMA, JawabanPenyisihanSMP,
    SoalPenyisihanSD,
    SoalPenyisihanSMP,
    SoalPenyisihanSMA,
    JawabanPenyisihanSD,
)


class PenyisihanResultView(TemplateView):
    template_name = "penyisihans/result.html"

    def result(self, jawaban, peserta):
        kunciA, kunciB, kunciC, kunciD, kunciE = None, None, None, None, None
        if peserta.tingkat == 'SMA':
            kunciA = ["1A", "2E", "3D", "4B", "5C", "6B", "7C",
                      "8A", "9D", "10A", "11B", "12E", "13D", "14E", "15A"]
            kunciB = ["1E", "2D", "3B", "4C", "5B", "6C", "7A",
                      "8D", "9A", "10B", "11E", "12D", "13E", "14A", "15A"]
            kunciC = ["1D", "2B", "3C", "4B", "5C", "6A", "7D",
                      "8A", "9B", "10E", "11D", "12E", "13A", "14A", "15E"]
            kunciD = ["1B", "2C", "3B", "4C", "5A", "6D", "7A",
                      "8B", "9E", "10D", "11E", "12A", "13A", "14E", "15D"]
            kunciE = ["1C", "2B", "3C", "4A", "5D", "6A", "7B",
                      "8E", "9D", "10E", "11A", "12A", "13E", "14D", "15B"]

        if peserta.tingkat == 'SMP':
            kunciA = ["1C", "2A", "3C", "4A", "5B", "6B", "7D",
                      "8A", "9D", "10B", "11A", "12B", "13D", "14B", "15C"]
            kunciB = ["1A", "2C", "3A", "4B", "5B", "6D", "7A",
                      "8D", "9B", "10A", "11B", "12D", "13B", "14C", "15C"]
            kunciC = ["1C", "2B", "3D", "4B", "5A", "6B", "7D",
                      "8A", "9D", "10B", "11B", "12A", "13C", "14A", "15C"]
            kunciD = ["1B", "2D", "3B", "4A", "5B", "6D", "7A",
                      "8D", "9B", "10B", "11A", "12C", "13A", "14C", "15B"]
            kunciE = ["1B", "2A", "3C", "4A", "5C", "6B", "7D",
                      "8A", "9D", "10B", "11C", "12B", "13D", "14B", "15A"]

        if peserta.tingkat == 'SD':
            kunciA = ["1D", "2D", "3B", "4A", "5B", "6E", "7C",
                      "8C", "9D", "10B", "11B", "12A", "13A", "14E", "15B"]
            kunciB = ["1E", "2C", "3B", "4B", "5E", "6B", "7B",
                      "8D", "9C", "10B", "11C", "12D", "13D", "14C", "15A"]
            kunciC = ["1B", "2A", "3B", "4D", "5E", "6C", "7B",
                      "8E", "9A", "10C", "11C", "12A", "13A", "14B", "15C"]
            kunciD = ["1C", "2E", "3B", "4B", "5D", "6D", "7C",
                      "8A", "9B", "10A", "11B", "12A", "13C", "14E", "15B"]
            kunciE = ["1A", "2B", "3B", "4C", "5A", "6B", "7A",
                      "8E", "9D", "10B", "11E", "12C", "13B", "14C", "15D"]
        benar, salah, kosong, poin = 0, 0, 0, 0
        paket_soal = jawaban.paket_soal

        jawaban = jawaban.jawaban_peserta.split()
        if paket_soal == "A":
            for i in range(len(jawaban)):
                if jawaban[i].isdigit():
                    kosong += 1
                elif kunciA[i] == jawaban[i]:
                    poin += 4
                    benar += 1
                else:
                    salah += 1
                    poin -= 2

        if paket_soal == "B":
            for i in range(len(jawaban)):
                if jawaban[i].isdigit():
                    kosong += 1
                elif kunciB[i] == jawaban[i]:
                    poin += 4
                    benar += 1
                else:
                    salah += 1
                    poin -= 2

        if paket_soal == "C":
            for i in range(len(jawaban)):
                if jawaban[i].isdigit():
                    kosong += 1
                elif kunciC[i] == jawaban[i]:
                    poin += 4
                    benar += 1
                else:
                    salah += 1
                    poin -= 2

        if paket_soal == "D":
            for i in range(len(jawaban)):
                if jawaban[i].isdigit():
                    kosong += 1
                elif kunciD[i] == jawaban[i]:
                    poin += 4
                    benar += 1
                else:
                    salah += 1
                    poin -= 2

        if paket_soal == "E":
            for i in range(len(jawaban)):
                if jawaban[i].isdigit():
                    kosong += 1
                elif kunciE[i] == jawaban[i]:
                    poin += 4
                    benar += 1
                else:
                    salah += 1
                    poin -= 2

        data = [benar, salah, kosong, poin]

        return data

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])

        jawaban = None
        if peserta.tingkat == 'SD':
            jawaban = JawabanPenyisihanSD.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMP':
            jawaban = JawabanPenyisihanSMP.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMA':
            jawaban = JawabanPenyisihanSMA.objects.get(
                exam_code=kwargs["exam_code"])

        data = self.result(jawaban, peserta)
        print(data)
        jawaban.result_peserta = data[3]
        jawaban.jawaban_benar = data[0]
        jawaban.jawaban_salah = data[1]
        jawaban.jawaban_kosong = data[2]
        jawaban.save()

        context["jawaban"] = jawaban
        context['peserta'] = peserta
        return self.render_to_response(context)


# bukan view
# method untuk mengisi field jawaban peserta


def generate_jawaban(data):
    jawaban = ""
    for d in data:
        if d != "csrfmiddlewaretoken":
            jawaban += d + data[d] + " "

    return jawaban


# belum selesai untuk smp dan sma(soal dan jawaban)


def UjianPenyisihanView(request, *args, **kwargs):
    peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
    context = {}

    if request.method == "GET":
        # mengambil soal
        soal = None
        event = None
        if peserta.tingkat == "SD":
            soal = SoalPenyisihanSD.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SD")

        if peserta.tingkat == "SMP":
            soal = SoalPenyisihanSMP.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SMP")

        if peserta.tingkat == "SMA":
            soal = SoalPenyisihanSMA.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Penyisihan SMA")

        # data
        context = {
            "peserta": peserta,
            "soal": soal,
            "event": event,
        }

        from django.core.serializers import serialize
        data = serialize("json", soal)
        context["data"] = data

        context['time'] = datetime.now()
        from django.utils import timezone
        context['time2'] = timezone.now()

    if request.method == "POST":
        data = request.POST
        jawaban = generate_jawaban(data)
        if peserta.tingkat == "SD":
            jawaban_peserta = JawabanPenyisihanSD(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()
        if peserta.tingkat == "SMP":
            jawaban_peserta = JawabanPenyisihanSMP(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()
        if peserta.tingkat == "SMA":
            jawaban_peserta = JawabanPenyisihanSMA(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        success_url = reverse_lazy(
            "penyisihans:result", kwargs={"exam_code": peserta.exam_code}
        )
        return HttpResponseRedirect(success_url)

    return render(request, "penyisihans/ujian.html", context)


class StartPenyisihanView(TemplateView):
    template_name = "penyisihans/start.html"
    model = Participant

    def cek_paket(self, peserta):
        peserta = peserta
        if peserta.paket_soal == "":
            import random

            paket = "ABCDE"
            peserta.paket_soal = random.choice(paket)
            peserta.save()
            print("peserta paket", peserta.paket_soal)

    def get(self, request, *args, **kwargs):
        peserta = self.model.objects.get(exam_code=kwargs["exam_code"])
        event = None

        if peserta.tingkat == "SD":
            event = Event.objects.get(nama_event="Penyisihan SD")
        if peserta.tingkat == "SMP":
            event = Event.objects.get(nama_event="Penyisihan SMP")
        if peserta.tingkat == "SMA":
            event = Event.objects.get(nama_event="Penyisihan SMA")

        context = self.get_context_data(**kwargs)
        context["peserta"] = peserta
        context["event"] = event
        self.cek_paket(peserta)
        return self.render_to_response(context)
