from exams.models import JawabanFast
from exams.forms import JawabanBalloonForm
from django.views.generic import TemplateView

from participants.models import Participant


class PesertaFastGame:

    def __init__(self, peserta, jawaban):
        self.peserta = peserta
        self.jawaban = jawaban


class HomeDataView(TemplateView):
    template_name = 'data/home.html'

    def get(self, request, *args, **kwargs):
        peserta_sd = len(Participant.objects.filter(tingkat='SD'))

        # hasil fast game
        peserta = []
        peserta_fast_game = Participant.objects.filter(fastgame=True)
        for i in peserta_fast_game:
            jawaban_peserta_fastgame = JawabanFast.objects.filter(
                id_peserta=i.id)
            peserta.append(PesertaFastGame(i, jawaban_peserta_fastgame))

        self.extra_context = {
            'peserta_sd': peserta_sd,
            'peserta_fast_game': peserta,
        }
        return self.render_to_response(self.get_context_data())
