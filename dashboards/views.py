from theaters.models import JawabanTheaterModelSMA, JawabanTheaterModelSMP
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
from participants.models import Participant
from penyisihans.models import JawabanPenyisihanSD, JawabanPenyisihanSMP, JawabanPenyisihanSMA
from semifinals.models import JawabanSemifinalSD, JawabanSemifinalSMP, JawabanSemifinalSMA
from balloons.models import BalloonSoalModel
from fasts.models import JawabanFastModel
from theaters.models import JawabanTheaterModelSMA, JawabanTheaterModelSMP
from playoffs.models import PlayOffPenyisihan, PlayOffTheatre
from playoffs.models import PlayOffSemifinal


class GambaranUmum(TemplateView):
    template_name = 'dashboards/gambaran_umum.html'


class Jadwal(TemplateView):
    template_name = 'dashboards/jadwal.html'

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.all()

        for i in peserta:
            i.is_login = False
            i.save

        return self.render_to_response(self.get_context_data())


class DataViewSMA(TemplateView):
    template_name = "dashboards/datasma.html"

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.filter(
            tingkat="SMA").order_by('no_id')

        soalb = BalloonSoalModel.objects.all()
        for i in soalb:
            i.is_taken = False
            i.exam_code = ''
            i.jawaban = ''
            i.save()

        penyisihan = JawabanPenyisihanSMA.objects.order_by(
            "-result_peserta")
        playoff_penyisihan = PlayOffPenyisihan.objects.filter(tingkat='SMP')

        semifinal = JawabanSemifinalSMA.objects.order_by(
            "-result_peserta")
        playoff_semifinal = PlayOffSemifinal.objects.filter(tingkat='SMP')

        theater = JawabanTheaterModelSMA.objects.all().order_by('nama_peserta')
        playoff_theatre = PlayOffTheatre.objects.filter(tingkat='SMA')
        self.extra_context = {
            "peserta": peserta,
            "penyisihan": penyisihan,
            "playoff_penyisihan": playoff_penyisihan,
            "semifinal": semifinal,
            "playoff_semifinal": playoff_semifinal,
            "theater": theater,
            "playoff_theatre": playoff_theatre,
        }
        return self.render_to_response(self.get_context_data())


class DataViewSMP(TemplateView):
    template_name = 'dashboards/datasmp.html'

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.filter(
            tingkat="SMP").order_by('no_id')

        penyisihan = JawabanPenyisihanSMP.objects.order_by(
            "-result_peserta")
        playoff_penyisihan = PlayOffPenyisihan.objects.filter(tingkat='SMP')

        semifinal = JawabanSemifinalSMP.objects.order_by(
            "-result_peserta")
        playoff_semifinal = PlayOffSemifinal.objects.filter(tingkat='SMP')

        theater = JawabanTheaterModelSMP.objects.all().order_by('nama_peserta')
        playoff_theatre = PlayOffTheatre.objects.filter(tingkat='SMP')

        from django.core.serializers import serialize
        data = serialize("json", peserta)

        self.extra_context = {
            "peserta": peserta,
            "penyisihan": penyisihan,
            "playoff_penyisihan": playoff_penyisihan,
            "semifinal": semifinal,
            "playoff_semifinal": playoff_semifinal,
            "theater": theater,
            "playoff_theatre": playoff_theatre,
            "data": data,
        }
        return self.render_to_response(self.get_context_data())


class DataViewSD(TemplateView):
    template_name = "dashboards/datasd.html"

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.filter(
            tingkat="SD").order_by('no_id')

        penyisihan = JawabanPenyisihanSD.objects.order_by(
            "-result_peserta")

        playoff_penyisihan = PlayOffPenyisihan.objects.filter(tingkat='SD')

        semifinal = JawabanSemifinalSD.objects.order_by(
            "-result_peserta")

        playoff_semifinal = PlayOffSemifinal.objects.filter(tingkat='SD')

        fast = JawabanFastModel.objects.order_by(
            "-result_peserta")

        # baloon
        peserta_sd_baloon = Participant.objects.filter(
            tingkat="SD", balloongame=True)

        nama_peserta_sd_baloon = []
        for q in peserta_sd_baloon:
            nama_peserta_sd_baloon.append(q)

        list_jawaban_balloon = []
        for p in peserta_sd_baloon:
            jawaban = BalloonSoalModel.objects.filter(exam_code=p.exam_code)
            list_jawaban_balloon.append(jawaban)

        dict_jawaban = {}
        for o in range(len(nama_peserta_sd_baloon)):
            dict_jawaban[nama_peserta_sd_baloon[o].first_name] = list_jawaban_balloon[o]

        self.extra_context = {
            "peserta": peserta,
            "penyisihan": penyisihan,
            "playoff_penyisihan": playoff_penyisihan,
            "semifinal": semifinal,
            "playoff_semifinal": playoff_semifinal,
            "dict_jawaban": dict_jawaban,
            "fast": fast,
        }
        return self.render_to_response(self.get_context_data())


class AboutView(TemplateView):
    template_name = "dashboards/about.html"


class DocumentView(TemplateView):
    template_name = "dashboards/document.html"


class TutorialRegistrasiView(TemplateView):
    template_name = "dashboards/tutorial_registrasi.html"


class IndexView(TemplateView):
    template_name = "dashboards/index.html"

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.get(id=kwargs["user_id"])
        jawaban_penyisihan_sd = None
        jawaban_semifinal_sd = None

        jawaban_penyisihan_smp = None
        jawaban_semifinal_smp = None

        jawaban_penyisihan_sma = None
        jawaban_semifinal_sma = None

        jawaban_balloon = BalloonSoalModel.objects.filter(
            exam_code=peserta.exam_code)

        jawaban_fast = JawabanFastModel.objects.filter(
            exam_code=peserta.exam_code)

        jawaban_theatre = None
        if peserta.tingkat == "SMP":
            jawaban_theatre = JawabanTheaterModelSMP.objects.filter(
                exam_code=peserta.exam_code)

        if peserta.tingkat == "SMA":
            jawaban_theatre = JawabanTheaterModelSMA.objects.filter(
                exam_code=peserta.exam_code)

        try:
            jawaban_penyisihan_sd = JawabanPenyisihanSD.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanPenyisihanSD.DoesNotExist:
            print("Jawaban Penyisihan Not Found")

        try:
            jawaban_semifinal_sd = JawabanSemifinalSD.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanSemifinalSD.DoesNotExist:
            print("Jawaban Semifinal Not Found")

        try:
            jawaban_penyisihan_smp = JawabanPenyisihanSMP.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanPenyisihanSMP.DoesNotExist:
            print("Jawaban Penyisihan Not Found")

        try:
            jawaban_semifinal_smp = JawabanSemifinalSMP.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanSemifinalSMP.DoesNotExist:
            print("Jawaban Semifinal Not Found")

        try:
            jawaban_penyisihan_sma = JawabanPenyisihanSMA.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanPenyisihanSMA.DoesNotExist:
            print("Jawaban Penyisihan Not Found")

        try:
            jawaban_semifinal_sma = JawabanSemifinalSMA.objects.filter(
                exam_code=peserta.exam_code)

        except JawabanSemifinalSMA.DoesNotExist:
            print("Jawaban Semifinal Not Found")

        self.extra_context = {
            "peserta": peserta,
            "jawaban_penyisihan_sd": jawaban_penyisihan_sd,
            "jawaban_semifinal_sd": jawaban_semifinal_sd,
            "jawaban_penyisihan_smp": jawaban_penyisihan_smp,
            "jawaban_semifinal_smp": jawaban_semifinal_smp,
            "jawaban_penyisihan_sma": jawaban_penyisihan_sma,
            "jawaban_semifinal_sma": jawaban_semifinal_sma,
            "jawaban_balloon": jawaban_balloon,
            "jawaban_fast": jawaban_fast,
            "jawaban_theatre": jawaban_theatre,
        }
        return self.render_to_response(self.get_context_data())


class Home(TemplateView):
    template_name = "dashboards/home.html"
