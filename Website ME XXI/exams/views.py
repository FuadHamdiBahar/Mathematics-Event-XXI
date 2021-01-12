from django.contrib.auth.decorators import login_required
from django.db.models import fields
from django.http.response import Http404, HttpResponseRedirect
from django.urls.base import reverse
from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.urls import reverse_lazy
from django.shortcuts import render
# Create your views here.

# models
from .models import FastSoal, JawabanFast, JawabanSemiFinal, Soal, Jawaban, BalloonSoal, JawabanBalloon
from participants.models import Participant

# forms
from .forms import JawabanForm, JawabanBalloonForm, JawabanFastForm


class FinishView(TemplateView):
    template_name = 'exams/finish.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        # penyisihan
        try:
            jawaban = Jawaban.objects.get(id_peserta=kwargs['id'])
            context['jawaban'] = jawaban

            # memeriksa jawaban
            if jawaban.result == '':
                jawaban_benar = ['1B', '2D', '3A', '4E', '5B']

                jawaban_peserta = jawaban.jawaban_peserta.split(', ')
                del jawaban_peserta[0]
                sum = 0
                for i in jawaban_peserta:
                    if i in jawaban_benar:
                        sum += 1
                jawaban.result = sum
                jawaban.save()
        except Jawaban.DoesNotExist:
            context['jawaban'] = None

        # semifinal
        try:
            jawabansf = JawabanSemiFinal.objects.get(id_peserta=kwargs['id'])
            context['jawabansf'] = jawabansf
            # memeriksa jawaban
            if jawabansf.result == '':
                jawabansf_benar = ['6E', '7B', '8B', '9D', '10E']

                jawabansf_peserta = jawabansf.jawaban_peserta.split(', ')
                del jawabansf_peserta[0]
                sum = 0
                for i in jawabansf_peserta:
                    if i in jawabansf_benar:
                        sum += 1

                jawabansf.result = sum
                jawabansf.save()
        except JawabanSemiFinal.DoesNotExist:
            context['jawabansf'] = None

        return self.render_to_response(context)


class FastGameView(FormView):
    form_class = JawabanFastForm
    template_name = 'exams/fast.html'

    def get(self, request, *args, **kwargs):
        soal = FastSoal.objects.get(id=kwargs['id_soal'])
        self.extra_context = {
            'soal': soal,
        }
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, parameter=kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, parameter):
        data = form.cleaned_data

        soal = FastSoal.objects.get(id=parameter['id_soal'])
        peserta = Participant.objects.get(exam_code=parameter['exam_code'])
        print(peserta)

        new_jawaban = JawabanFast(
            id_soal=soal.id,
            nama_peserta=peserta.first_name,
            id_peserta=peserta.id,
            exam_code=peserta.exam_code,
            jawaban_peserta=data['jawaban_peserta'],
        )
        new_jawaban.save()

        if soal.id == 10:
            success_url = reverse_lazy(
                'exams:finish', kwargs={'id': peserta.id})
        else:
            success_url = reverse_lazy('exams:fast',
                                       kwargs={
                                           'exam_code': parameter['exam_code'],
                                           'id_soal': soal.id + 1
                                       })

        return HttpResponseRedirect(success_url)


class BalloonGameSoalView(FormView):
    form_class = JawabanBalloonForm
    template_name = 'exams/soal_balloon.html'

    def get(self, request, *args, **kwargs):
        soal = BalloonSoal.objects.get(
            id=kwargs['id_soal'])
        self.extra_context = {
            'soal': soal,
        }
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form, parameter=kwargs)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, parameter):
        data = form.cleaned_data
        peserta = Participant.objects.get(exam_code=parameter['exam_code'])
        soal = BalloonSoal.objects.get(id=parameter['id_soal'])

        new_jawaban = JawabanBalloon(
            nama_peserta=peserta.first_name,
            id_peserta=peserta.id,
            exam_code=peserta.exam_code,
            soal_peserta=soal.id,
            jawaban_peserta=data['jawaban_peserta']
        )
        new_jawaban.save()
        print(new_jawaban)
        success_url = reverse_lazy('exams:balloon', kwargs={
            'exam_code': parameter['exam_code']})

        return HttpResponseRedirect(success_url)


class BalloonGameDetailView(DetailView):
    model = BalloonSoal
    template_name = 'exams/detail_balloon.html'

    def get(self, request, *args, **kwargs):
        # soal untuk menampilkan soal acak
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        # soal seharusnya yg diperoleh dari soal acak
        soal = BalloonSoal.objects.get(id=kwargs['pk'])
        context['soal'] = soal
        print(soal)

        # is_taken soal sebelumnya
        if self.object.is_taken == False:
            self.object.exam_code = kwargs['exam_code']
            self.object.is_taken = True
            self.object.save()

        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        context['peserta'] = peserta

        return self.render_to_response(context)


class BalloonGameView(TemplateView):
    template_name = 'exams/balloon.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        soal = BalloonSoal.objects.filter(is_taken=False)
        context['soal'] = soal

        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        context['peserta'] = peserta
        return self.render_to_response(context)


@login_required
def SemiFinal(request, *args, **kwargs):
    context = {}
    if request.method == 'GET':
        soal = Soal.objects.filter(kategori='Semifinal').filter(
            tingkat=kwargs['tingkat'])

        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        context['peserta'] = peserta

        try:
            jawaban = JawabanSemiFinal.objects.get(
                exam_code=kwargs['exam_code'])
            context['jawaban'] = jawaban
        except JawabanSemiFinal.DoesNotExist:
            context['jawaban'] = None

        context['soal'] = soal

    if request.method == 'POST':
        data = request.POST
        participant = Participant.objects.get(exam_code=kwargs['exam_code'])

        jawaban = ''
        for i in data:
            jawaban += i + str(data[i]) + ', '

        new_jawaban = JawabanSemiFinal(
            nama_peserta=participant.first_name,
            id_peserta=participant.id,
            exam_code=kwargs['exam_code'],
            jawaban_peserta=jawaban,
        )
        new_jawaban.save()

        success_url = reverse_lazy('exams:finish', kwargs={
                                   'id': participant.id})
        return HttpResponseRedirect(success_url)

    return render(request, 'exams/semifinal.html', context)


@login_required
def BabakPenyisihan3(request, *args, **kwargs):
    context = {}
    if request.method == 'GET':
        soal = Soal.objects.filter(kategori='Penyisihan').filter(
            tingkat=kwargs['tingkat'])
        context['soal'] = soal

        peserta = Participant.objects.get(exam_code=kwargs['exam_code'])
        context['peserta'] = peserta

        try:
            jawaban = Jawaban.objects.get(exam_code=kwargs['exam_code'])
            context['jawaban'] = jawaban
        except Jawaban.DoesNotExist:
            context['jawaban'] = None

    if request.method == 'POST':
        data = request.POST
        participant = Participant.objects.get(exam_code=kwargs['exam_code'])
        jawaban = ''
        for i in data:
            jawaban += i + str(data[i]) + ', '

        new_jawaban = Jawaban(
            nama_peserta=participant.first_name,
            id_peserta=participant.id,
            exam_code=kwargs['exam_code'],
            tingkat=participant.tingkat,
            jawaban_peserta=jawaban,
        )
        new_jawaban.save()

        success_url = reverse_lazy('exams:finish', kwargs={
                                   'id': participant.id})
        return HttpResponseRedirect(success_url)
    return render(request, 'exams/penyisihan3.html', context)


class BabakPenyisihan2(FormView):
    form_class = JawabanForm
    model = Jawaban
    fields = []
    template_name = 'exams/penyisihan2.html'

    def get(self, request, *args, **kwargs):
        soal = Soal.objects.get(id=kwargs['id_soal'])
        participant = Participant.objects.get(exam_code=kwargs['exam_code'])
        self.extra_context = {
            'soal': soal,
            'participant': participant,
        }
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        parameter = kwargs
        if form.is_valid():
            return self.form_valid(form, parameter)
        else:
            return self.form_invalid(form)

    def form_valid(self, form, parameter):
        form = form.cleaned_data

        # mengambil informasi yg dibutuhkan
        participant = Participant.objects.get(exam_code=parameter['exam_code'])
        soal = Soal.objects.get(id=parameter['id_soal'])

        new_jawaban = Jawaban(
            kode_soal=soal.kategori + parameter['id_soal'],
            id_participant=participant.id,
            exam_code_participant=participant.exam_code,
            jawaban_peserta=form['jawaban_peserta'],
            jawaban_benar=soal.jawaban_benar,
        )
        new_jawaban.save()

        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)


class BabakPenyisihan(ListView):
    queryset = Soal.objects.all().filter(kategori='Penyisihan')
    template_name = 'exams/penyisihan.html'
    paginate_by = 1

    def get_participant(self, exam_code):
        participant = Participant.objects.get(exam_code=exam_code)
        return participant

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty:
            if self.get_paginate_by(self.object_list) is not None and hasattr(self.object_list, 'exists'):
                is_empty = not self.object_list.exists()
            else:
                is_empty = not self.object_list
            if is_empty:
                raise Http404(_('Empty list and “%(class_name)s.allow_empty” is False.') % {
                    'class_name': self.__class__.__name__,
                })
        context = self.get_context_data()
        context['soal'] = context['object_list'][0]
        context['queryset'] = self.object_list

        # mendapatkan participant
        peserta = self.get_participant(kwargs['exam_code'])
        context['peserta'] = peserta

        print(context['soal'])
        return self.render_to_response(context)
