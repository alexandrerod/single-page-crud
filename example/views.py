from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from example.forms import ArvoreModelForm
from example.models import Arvore


def index(request):
    return render(request, 'example/index.html')


def list_equipaments(request):
    data = {}
    queryset = Arvore.objects.all()
    context = {'equipamentos': queryset}
    data['html_list'] = render_to_string('example/list.html',
                                         context,
                                         )

    return JsonResponse(data)


def save_form(request, form, template_name):
    data = dict()

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
        else:
            data['form_is_valid'] = False

    context = {'form': form}

    data['html_form'] = render_to_string(template_name, context, request=request)

    return JsonResponse(data)


def create_equipaments(request):

    if request.method == 'POST':
        form = ArvoreModelForm(request.POST)
    else:
        form = ArvoreModelForm()

    return save_form(request, form, 'example/create.html')


def update_equipaments(request, id):
    queryset = get_object_or_404(Arvore, pk=id)
    if request.method == 'POST':
        form = ArvoreModelForm(request.POST, instance=queryset)
    else:
        form=ArvoreModelForm(instance=queryset)

    return save_form(request, form, 'example/update.html')

