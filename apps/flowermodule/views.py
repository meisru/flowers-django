from django.shortcuts import render
from django.db.models import Q
from .models import Flower


def home(request):
    featured = Flower.objects.all()[:3]
    return render(request, 'flowermodule/home.html', {'featured': featured})


def flowers(request):
    all_flowers = Flower.objects.all().order_by('name')
    return render(request, 'flowermodule/flowers.html', {'flowers': all_flowers})


def about(request):
    total   = Flower.objects.count()
    origins = Flower.objects.values_list('origin', flat=True).distinct().count()
    return render(request, 'flowermodule/about.html', {'total': total, 'origins': origins})


def search(request):
    query   = request.GET.get('q', '').strip()
    color   = request.GET.get('color', '').strip()
    results = None

    if query or color:
        results = Flower.objects.all()
        if query:
            results = results.filter(
                Q(name__icontains=query) |
                Q(scientific_name__icontains=query) |
                Q(description__icontains=query) |
                Q(origin__icontains=query)
            )
        if color:
            results = results.filter(color__icontains=color)

    colors = Flower.objects.values_list('color', flat=True).distinct()
    return render(request, 'flowermodule/search.html', {
        'results': results,
        'query':   query,
        'color':   color,
        'colors':  colors,
    })
