from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from datetime import datetime
from django.views.generic import TemplateView

# Create your views here.
from participants.models import Participant
from semifinals.models import (
    Event,
    SoalSemifinalSD,
    SoalSemifinalSMP,
    SoalSemifinalSMA,
    JawabanSemifinalSD,
    JawabanSemifinalSMP,
    JawabanSemifinalSMA,
)


class SemifinalResultView(TemplateView):
    template_name = "semifinals/result.html"

    def result(self, jawaban, peserta):
        kunciA, kunciB, kunciC, kunciD, kunciE = None, None, None, None, None
        if peserta.tingkat == 'SMA':
            kunciA = ['1D', '2B', '3D', '4D', '5E', '6C', '7B',
                      '8A', '9C', '10A', '11D', '12B', '13E', '14D', '15B']
            kunciB = ['1B', '2D', '3D', '4E', '5C', '6B', '7A',
                      '8C', '9A', '10D', '11B', '12E', '13D', '14B', '15D']
            kunciC = ['1D', '2D', '3E', '4C', '5B', '6A', '7C',
                      '8A', '9D', '10B', '11E', '12D', '13B', '14D', '15B']
            kunciD = ['1D', '2E', '3C', '4B', '5A', '6C', '7A',
                      '8D', '9B', '10E', '11D', '12B', '13D', '14B', '15D']
            kunciE = ['1E', '2C', '3B', '4A', '5C', '6A', '7D',
                      '8B', '9E', '10D', '11B', '12D', '13B', '14D', '15D']

        if peserta.tingkat == 'SMP':
            kunciA = ["1B", "2A", "3D", "4B", "5D", "6A", "7C",
                      "8D", "9B", "10B", "11D", "12D", "13D", "14B", "15A"]
            kunciB = ["1A", "2D", "3B", "4D", "5A", "6C", "7D",
                      "8B", "9B", "10D", "11D", "12D", "13B", "14A", "15B"]
            kunciC = ["1A", "2B", "3D", "4D", "5D", "6B", "7B",
                      "8D", "9C", "10A", "11D", "12B", "13D", "14A", "15B"]
            kunciD = ["1B", "2D", "3D", "4D", "5B", "6B", "7D",
                      "8C", "9A", "10D", "11B", "12D", "13A", "14C", "15A"]
            kunciE = ["1D", "2B", "3D", "4A", "5B", "6B", "7B",
                      "8D", "9C", "10A", "11A", "12B", "13D", "14D", "15D"]

        if peserta.tingkat == 'SD':
            kunciA = ["1C", "2D", "3E", "4B", "5A", "6D", "7A",
                      "8D", "9D", "10A", "11C", "12C", "13A", "14C", "15B"]
            kunciB = ["1D", "2E", "3B", "4A", "5D", "6A", "7D",
                      "8D", "9A", "10C", "11C", "12A", "13C", "14B", "15C"]
            kunciC = ["1E", "2B", "3A", "4D", "5A", "6D", "7D",
                      "8A", "9C", "10C", "11A", "12C", "13B", "14C", "15D"]
            kunciD = ["1B", "2A", "3D", "4A", "5D", "6D", "7A",
                      "8C", "9C", "10A", "11C", "12B", "13C", "14D", "15E"]
            kunciE = ["1A", "2D", "3A", "4D", "5D", "6A", "7C",
                      "8C", "9A", "10C", "11B", "12C", "13D", "14E", "15B"]
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
            jawaban = JawabanSemifinalSD.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMP':
            jawaban = JawabanSemifinalSMP.objects.get(
                exam_code=kwargs["exam_code"])
        if peserta.tingkat == 'SMA':
            jawaban = JawabanSemifinalSMA.objects.get(
                exam_code=kwargs["exam_code"])

        data = self.result(jawaban, peserta)
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


def UjianSemifinalView(request, *args, **kwargs):
    peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
    context = {}

    if request.method == "GET":
        # mengambil soal
        print("get test")
        soal = None
        event = None
        if peserta.tingkat == "SD":
            soal = SoalSemifinalSD.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Semifinal SD")

        if peserta.tingkat == "SMP":
            soal = SoalSemifinalSMP.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Semifinal SMP")

        if peserta.tingkat == "SMA":
            soal = SoalSemifinalSMA.objects.filter(
                paket_soal=peserta.paket_soal)
            event = Event.objects.get(nama_event="Semifinal SMA")

        context = {
            "peserta": peserta,
            "soal": soal,
            "event": event,
        }

        from django.core.serializers import serialize

        data = serialize("json", soal)
        context["data"] = data

    if request.method == "POST":
        print("post test")
        data = request.POST
        jawaban = generate_jawaban(data)
        if peserta.tingkat == "SD":
            jawaban_peserta = JawabanSemifinalSD(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        if peserta.tingkat == "SMP":
            jawaban_peserta = JawabanSemifinalSMP(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        if peserta.tingkat == "SMA":
            jawaban_peserta = JawabanSemifinalSMA(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                institusi_peserta=peserta.institusi_peserta,
                exam_code=peserta.exam_code,
                paket_soal=peserta.paket_soal,
                jawaban_peserta=jawaban,
            )
            jawaban_peserta.save()

        success_url = reverse_lazy(
            "semifinals:result", kwargs={"exam_code": peserta.exam_code}
        )
        return HttpResponseRedirect(success_url)

    return render(request, "semifinals/ujian.html", context)


class StartSemiFinalsView(TemplateView):
    model = Participant
    template_name = "semifinals/start.html"

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
            event = Event.objects.get(nama_event="Semifinal SD")
        if peserta.tingkat == "SMP":
            event = Event.objects.get(nama_event="Semifinal SMP")
        if peserta.tingkat == "SMA":
            event = Event.objects.get(nama_event="Semifinal SMA")

        context = self.get_context_data(**kwargs)
        context["peserta"] = peserta
        context["event"] = event
        self.cek_paket(peserta)
        return self.render_to_response(context)
