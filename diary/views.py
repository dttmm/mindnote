from django.shortcuts import render
from .models import Page
from .forms import PageForm

# Create your views here.


def page_list(request):
    context = dict()
    pages = Page.objects.all()
    context["pages"] = pages
    return render(request, 'diary/page_list.html', context)


def page_detail(request, page_id):
    context = dict()
    page = Page.objects.get(id=page_id)
    context["object"] = page
    return render(request, 'diary/page_detail.html', context)


def info(request):
    return render(request, 'diary/info.html')


def page_create(request):
    form = PageForm()
    context = dict()
    context["form"] = form
    return render(request, 'diary/page_form.html', context)
