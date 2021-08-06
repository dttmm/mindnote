from django.shortcuts import render, redirect
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
    if request.method == 'POST':
        page_form = PageForm(request.POST)
        if page_form.is_valid():
            new_page = page_form.save()
            return redirect('page-detail', page_id=new_page.id)

    else:
        page_form = PageForm()
    context = dict()
    context["form"] = page_form
    return render(request, 'diary/page_form.html', context)


def page_update(request, page_id):
    page = Page.objects.get(id=page_id)
    if request.method == 'POST':
        page_form = PageForm(request.POST, instance=page)
        if page_form.is_valid():
            page_form.save()
            return redirect('page-detail', page_id=page_id)
    else:
        page_form = PageForm(instance=page)
    return render(request, 'diary/page_form.html', {'form': page_form})
