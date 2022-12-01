from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import FormView

from .models import Institution

from .forms import InstitutionForm


class CreateInstitutionView(FormView):
    form_class = InstitutionForm
    template_name = 'institutions/create.html'
    success_url = 'dashboards:home'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        messages.add_message(request, messages.SUCCESS,
                             'Sekolah berhasil dibuat!')
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form = form.cleaned_data
        print(form)
        new_institusi = Institution(
            nama_sekolah=form['nama_sekolah'],
            provinsi_sekolah=form['provinsi_sekolah'],
            kabupaten_sekolah=form['kabupaten_sekolah'],
            kecamatan_sekolah=form['kecamatan_sekolah'],
            alamat_sekolah=form['alamat_sekolah'],
            email_sekolah=form['email_sekolah'],
            kontak_guru_pendamping=form['kontak_guru_pendamping'],
            kontak_sekolah=form['kontak_sekolah']
        )
        new_institusi.save()

        success_url = reverse_lazy('accounts:create')
        return HttpResponseRedirect(success_url)
