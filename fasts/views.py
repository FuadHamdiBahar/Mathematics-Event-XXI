from participants.models import Participant
from django.shortcuts import render
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

# Create your views here.
from .models import Event, SoalFastModel, JawabanFastModel


def generate_jawaban(data):
    jawaban = ''
    for d in data:
        if d != 'csrfmiddlewaretoken':
            jawaban += d + data[d] + ' '

    return jawaban


def UjianFastView(request, *args, **kwargs):
    peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
    context = {}
    if request.method == 'GET':
        soal = SoalFastModel.objects.all()
        event = Event.objects.get(id=1)
        context = {
            'soal': soal,
            'peserta': peserta,
            'event': event,
        }

        from django.core.serializers import serialize
        data = serialize('json', soal)
        context['data'] = data

    if request.method == 'POST':
        data = request.POST
        jawaban = generate_jawaban(data)
        jawaban_peserta = JawabanFastModel(
            id_peserta=peserta.no_id,
            nama_peserta=peserta.first_name,
            exam_code=peserta.exam_code,
            paket_soal=peserta.paket_soal,
            jawaban_peserta=jawaban,
        )
        jawaban_peserta.save()

        success_url = reverse_lazy('fasts:result', kwargs={
                                   'exam_code': peserta.exam_code})
        return HttpResponseRedirect(success_url)

    return render(request, 'fasts/ujian.html', context)


class StartFastView(TemplateView):
    template_name = 'fasts/start.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        context['peserta'] = peserta
        context['event'] = Event.objects.get(id=1)
        return self.render_to_response(context)


class JawabanResultView(TemplateView):
    template_name = "fasts/result.html"

    def result(self, jawaban):
        kunci = ["1C", "2C", "3B", "4A", "5B", "6D", "7B", "8B",
                 "9A", "10B"]
        benar, salah, kosong, poin = 0, 0, 0, 0
        paket_soal = jawaban.paket_soal

        jawaban = jawaban.jawaban_peserta.split()
        for i in range(len(jawaban)):
            if jawaban[i].isdigit():
                kosong += 1
            elif kunci[i] == jawaban[i]:
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
        jawaban = JawabanFastModel.objects.get(
            exam_code=kwargs["exam_code"])

        data = self.result(jawaban)
        jawaban.result_peserta = data[3]
        jawaban.jawaban_benar = data[0]
        jawaban.jawaban_salah = data[1]
        jawaban.jawaban_kosong = data[2]
        jawaban.save()

        context["jawaban"] = jawaban
        context['peserta'] = peserta
        return self.render_to_response(context)
