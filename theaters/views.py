from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

# Create your views here.

from participants.models import Participant
from .models import (
    JawabanTheaterModelSMP,
    JawabanTheaterModelSMA,
    Event
)


class ResultView(TemplateView):
    template_name = 'theaters/result.html'


def UjianTheatreView(request, *args, **kwargs):
    context = {}
    if request.method == 'GET':
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])

        event = None
        if peserta.tingkat == 'SMP':
            event = Event.objects.get(id=1)

        if peserta.tingkat == 'SMA':
            event = Event.objects.get(id=6)

        context = {
            "event": event,
        }

    if request.method == 'POST':
        data = request.POST
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        jawaban = []
        for i in data:
            if i != 'csrfmiddlewaretoken':
                jawaban.append(str(i) + "." + data[i])

        if peserta.tingkat == "SMP":
            jawaban_theater = JawabanTheaterModelSMP(
                exam_code=kwargs["exam_code"],
                nama_peserta=Participant.objects.get(
                    exam_code=kwargs["exam_code"]
                ).first_name,
                jawaban=jawaban,
            )
            jawaban_theater.save()

        if peserta.tingkat == "SMA":
            jawaban_theater = JawabanTheaterModelSMA(
                exam_code=kwargs["exam_code"],
                nama_peserta=Participant.objects.get(
                    exam_code=kwargs["exam_code"]
                ).first_name,
                jawaban=jawaban,
            )
            jawaban_theater.save()

        success_url = reverse_lazy("dashboards:index", kwargs={
            "user_id": peserta.id})
        return HttpResponseRedirect(success_url)
    return render(request, "theaters/ujian.html", context)


class StartTheaterView(TemplateView):
    template_name = "theaters/start.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        peserta = Participant.objects.get(exam_code=kwargs["exam_code"])
        context["peserta"] = peserta
        event = None
        if peserta.tingkat == "SMP":
            event = Event.objects.get(nama_event="Theatre SMP")

        if peserta.tingkat == 'SMA':
            event = Event.objects.get(nama_event="Theatre SMA")

        context["event"] = event
        return self.render_to_response(context)
