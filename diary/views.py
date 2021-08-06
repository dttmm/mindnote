from django.shortcuts import render, redirect
from .models import Page
from .forms import PageForm
from django.core.paginator import Paginator

# Create your views here.


def page_list(request):
    pages = Page.objects.all()
    paginator = Paginator(pages, 8)
    cur_page_num = request.GET.get('page')
    if cur_page_num == None:
        cur_page_num = 1
    page = paginator.page(cur_page_num)
    return render(request, 'diary/page_list.html', {"page": page})


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


def page_delete(request, page_id):
    page = Page.objects.get(id=page_id)
    if request.method == 'POST':
        page.delete()
        return redirect('page-list')
    else:
        return render(request, 'diary/page_confirm_delete.html', {'page': page})


def index(request):
    return render(request, 'diary/index.html')
