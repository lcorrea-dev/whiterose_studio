from django.shortcuts import render
from django.http import HttpResponse
from .models import GalleryImage
# Create your views here.


def gallery(request):
    imgs = GalleryImage.objects.all()
    context = {'imgs': imgs}
    return render(request, 'gallery/home.html', context)
