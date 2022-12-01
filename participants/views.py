import hashlib
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.urls.base import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect

# import ccbv
from django.views.generic import FormView
from django.contrib.auth.views import LoginView, LogoutView

# import models
from .models import Participant

# import forms
from .forms import ParticipantForm


def logout_request(request):
    peserta = Participant.objects.get(username=request.user)
    peserta.is_login = False
    peserta.save()
    logout(request)
    messages.info(request, "Anda berhasil logout!")
    return redirect("/")


class LoginParticipantView(LoginView):
    template_name = 'participants/login.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        username = request.POST['username']
        peserta = None
        try:
            peserta = Participant.objects.get(username=username)
        except Participant.DoesNotExist:
            messages.add_message(
                request, messages.WARNING, 'Username dan Password anda tidak benar!')
            success_url = reverse_lazy("accounts:login")
            return HttpResponseRedirect(success_url)

        print(peserta.is_login)
        if peserta.is_login == False:
            if form.is_valid():
                messages.add_message(request, messages.SUCCESS,
                                     'Anda berhasil Login')
                peserta.is_login = True
                peserta.save()
                print(peserta.is_login)
                return self.form_valid(form)
            else:
                messages.add_message(
                    request, messages.WARNING, 'Username dan Password anda tidak benar!')
                return self.form_invalid(form)
        else:
            messages.add_message(
                request, messages.WARNING, 'Akun sedang digunakan!')
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
            nisn_peserta=form['nisn_peserta'],
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
        success_url = reverse_lazy('accounts:login')
        return HttpResponseRedirect(success_url)
