from django import forms
from django.forms import fields

from .models import PlayOffPenyisihan, PlayOffSemifinal


class FormPlayOffPenyisihan(forms.ModelForm):
    class Meta:
        model = PlayOffPenyisihan
        fields = ['jawaban']
        widgets = {
            'jawaban': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }


class FormPlayOffSemifinal(forms.ModelForm):
    class Meta:
        model = PlayOffSemifinal
        fields = ['jawaban']
        widgets = {
            'jawaban': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
