# from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')

def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort', 'id')
    if sort_type == 'name':
        objects_phones = Phone.objects.order_by('name')
    elif sort_type == 'min_price':
        objects_phones = Phone.objects.order_by('price')
    elif sort_type == 'max_price':
        objects_phones = Phone.objects.order_by('-price')
    else:
        objects_phones = Phone.objects.order_by('id')
    context = {'phones': objects_phones, 'sort-item': sort_type}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)

