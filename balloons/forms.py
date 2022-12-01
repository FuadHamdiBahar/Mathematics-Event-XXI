from django import forms


from .models import BalloonSoalModel


class JawabanBalloonForm(forms.ModelForm):
    class Meta:
        model = BalloonSoalModel
        fields = ['jawaban']

        widgets = {
            'jawaban': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
        }
