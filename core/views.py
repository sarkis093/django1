from email import charset
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader
from .models import Produto

# Create your views here from templates folder (templates/).

def index(req):
    # print(dir(req))
    # print(req.session)
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos
        }
    return render(req, 'index.html', context)


def product(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)

    context = {
        'produto': prod
    }
    return render(request, 'product.html', context)


def contact(req):
    return render(req, 'contact.html')


def courses(req):
    context = {
        "curso" : {'curso1': 'Pentest', 'curso2': 'cybersecurity'}
        }
    return render(req, 'courses.html', context=context)


def error404(req, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=404)


def error500(req):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf-8', status=500)
