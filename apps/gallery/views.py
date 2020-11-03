from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import GalleryImage
# Create your views here.

IMGS_BY_PAGE = 9


def display_gallery(request):
    imgs = GalleryImage.objects.all()

    paginator = Paginator(imgs, IMGS_BY_PAGE)

    page_number = request.GET.get('page')
    selected_imgs = paginator.get_page(page_number)

    context = {'imgs': selected_imgs}

    return render(request, 'gallery/home.html', context)
