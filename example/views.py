from django.views.generic import ListView

from example.models import OrdemDeServico


class ListViews(ListView):
    queryset = OrdemDeServico.objects.all()
    context_object_name = 'ordens'
    template_name = 'example/index.html'
    paginate_by = 10
