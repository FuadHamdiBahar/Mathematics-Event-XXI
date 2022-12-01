
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect


# Create your views here.
from .forms import FormPlayOffPenyisihan, FormPlayOffSemifinal
from participants.models import Participant
from .models import (
    SoalPlayoff,
    PlayOffFast,
    PlayOffPenyisihan,
    PlayOffSemifinal,
    PlayOffBalloon,
    PlayOffTheatre
)


class StartPlayoffView(TemplateView):
    template_name = 'playoffs/start.html'

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        self.extra_context = {
            'peserta': peserta,
        }
        return self.render_to_response(self.get_context_data())


class UjianPlayoffView(FormView):
    form_class = FormPlayOffPenyisihan
    success_url = '/'
    template_name = 'playoffs/ujian.html'

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        soal = None

        if peserta.tingkat == 'SD':
            soal = SoalPlayoff.objects.get(id=1)
        if peserta.tingkat == 'SMP':
            soal = SoalPlayoff.objects.get(id=2)
        if peserta.tingkat == 'SMA':
            soal = SoalPlayoff.objects.get(id=3)

        self.extra_context = {
            'peserta': peserta,
            'soal': soal,
        }
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, kwargs):
        form = form.cleaned_data
        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        soal = None

        if peserta.tingkat == 'SD':
            soal = SoalPlayoff.objects.get(id=1)
        if peserta.tingkat == 'SMP':
            soal = SoalPlayoff.objects.get(id=2)
        if peserta.tingkat == 'SMA':
            soal = SoalPlayoff.objects.get(id=3)

        print(soal)
        jawaban = None
        if soal.babak == 'penyisihan':
            jawaban = PlayOffPenyisihan(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                jawaban=form['jawaban'],
                tingkat=peserta.tingkat
            )
        if soal.babak == 'semifinal':
            jawaban = PlayOffSemifinal(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                jawaban=form['jawaban'],
                tingkat=peserta.tingkat
            )
        if soal.babak == 'fast':
            jawaban = PlayOffFast(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                jawaban=form['jawaban'],
            )

        if soal.babak == 'balloon':
            jawaban = PlayOffBalloon(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                jawaban=form['jawaban'],
            )

        if soal.babak == 'theatre':
            jawaban = PlayOffTheatre(
                id_peserta=peserta.no_id,
                nama_peserta=peserta.first_name,
                jawaban=form['jawaban'],
                tingkat=peserta.tingkat
            )

        jawaban.save()
        success_url = '/'
        return HttpResponseRedirect(success_url)
