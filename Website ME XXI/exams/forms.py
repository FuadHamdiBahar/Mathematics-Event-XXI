from django import forms
from django.forms import widgets

from .models import Jawaban, JawabanBalloon, JawabanFast


class JawabanForm(forms.ModelForm):
    class Meta:
        model = Jawaban
        fields = ['jawaban_peserta']

        widgets = {
            'jawaban_peserta': forms.RadioSelect(
                attrs={
                    'class': 'custom-control-input'
                }
            ),
        }


class JawabanBalloonForm(forms.ModelForm):
    class Meta:
        model = JawabanBalloon
        fields = ['jawaban_peserta']

        widgets = {
            'jawaban_peserta': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class JawabanFastForm(forms.ModelForm):
    class Meta:
        model = JawabanFast
        fields = ['jawaban_peserta']

        widgets = {
            'jawaban_peserta': forms.Textarea(
                attrs={
                    'class': 'form-control',
                }
            )
        }
