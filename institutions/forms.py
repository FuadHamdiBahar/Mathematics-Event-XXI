from django import forms

from .models import Institution


class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = '__all__'

        widgets = {
            'nama_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'provinsi_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'kabupaten_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'kecamatan_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'alamat_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'email_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'kontak_guru_pendamping': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'kontak_sekolah': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
