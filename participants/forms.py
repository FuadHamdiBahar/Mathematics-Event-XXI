from django import forms
from django.forms import fields
from .models import Participant


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'first_name',
            'nisn_peserta',
            'jenis_kelamin',
            'institusi_peserta',
            'tingkat',
            'kontak_peserta',
            'email_peserta',
            'username',
            'password',
            'foto_peserta',
            'foto_rapor',
        ]

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'nisn_peserta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'contoh: 0001710121',
                }
            ),
            'jenis_kelamin': forms.Select(
                attrs={
                    'class': 'custom-select',
                }
            ),
            'institusi_peserta': forms.Select(
                attrs={
                    'class': 'custom-select',
                }
            ),
            'tingkat': forms.Select(
                attrs={
                    'class': 'custom-select',
                }
            ),
            'kontak_peserta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'contoh: 085111222333'
                }
            ),
            'email_peserta': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'type': 'email',
                }
            ),
            'password': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
