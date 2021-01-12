import hashlib
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password

# import ccbv
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView

# import models
from . models import Participant

# import forms
from .forms import ParticipantForm


class LogoutParticipantView(LogoutView):
    template_name = 'participants/logout.html'
    next_page = 'home'


class LoginParticipantView(LoginView):
    template_name = 'participants/login.html'
    success_url = reverse_lazy('dashboards:index')

    def post(self, request, *args, **kwargs):
        messages.add_message(request, messages.SUCCESS, 'Anda berhasil Login')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CreateParticipantView(FormView):
    form_class = ParticipantForm
    template_name = 'participants/create.html'

    def get(self, request, *args, **kwargs):
        peserta_terakhir = Participant.objects.filter(tingkat='SD').last()
        print(peserta_terakhir)
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            messages.add_message(request, messages.SUCCESS,
                                 'Akun anda berhasil dibuat!')
            return self.form_valid(form)
        else:
            messages.add_message(
                request, messages.WARNING, 'Form tidak valid!')
            print('masuk')
            return self.form_invalid(form)

    def generate_code(self, kata):
        kata = kata.encode()
        result = hashlib.sha1(kata)
        return str(result.hexdigest())

    def form_valid(self, form):
        form = form.cleaned_data
        form['password'] = make_password(form['password'])

        kata = form['tingkat'] + form['username']
        generate_code = self.generate_code(kata)
        print(form)

        new_participant = Participant(
            first_name=form['first_name'],
            username=form['username'],
            nis_peserta=form['nis_peserta'],
            jenis_kelamin=form['jenis_kelamin'],
            institusi_peserta=form['institusi_peserta'],
            tingkat=form['tingkat'],
            kontak_peserta=form['kontak_peserta'],
            email_peserta=form['email_peserta'],
            password=form['password'],
            foto_peserta=form['foto_peserta'],
            foto_rapor=form['foto_rapor'],
            exam_code=generate_code,
        )
        new_participant.save()

        print(new_participant)
        success_url = reverse_lazy('home')
        return HttpResponseRedirect(success_url)
