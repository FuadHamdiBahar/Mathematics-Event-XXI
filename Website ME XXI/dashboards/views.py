from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import TemplateView

from participants.models import Participant


@method_decorator(login_required, name='get')
class IndexView(TemplateView):
    template_name = 'dashboards/index.html'

    def get(self, request, *args, **kwargs):
        peserta = Participant.objects.get(id=kwargs['user_id'])
        self.extra_context = {
            'peserta': peserta,
        }
        return self.render_to_response(self.get_context_data())
