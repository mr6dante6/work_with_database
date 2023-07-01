from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_param = request.GET.get('sort')

    if sort_param == 'name':
        phones = Phone.objects.order_by('name')
    elif sort_param == 'min_price':
        phones = Phone.objects.order_by('price')
    else:
        phones = Phone.objects.order_by('-price', 'name')

    context = {
        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug=slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
