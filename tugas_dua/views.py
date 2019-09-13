from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
from PIL import Image as Pil
import os
SIZE_NOW = (0, 0)
TEMPORARY_IMAGE = "/static/tmp/temporary_image.jpg"

# Create your views here.
def viewIndex(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid(): form.save()
        else: form = ImageForm

        context = {
            'title': "Tugas Dua",
            'images': Image.objects.all(),
            'form': form
        }
        return render(request, 'tugas_dua/index.html', context)


def viewImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")
    
    if os.path.exists(TEMPORARY_IMAGE[1:]):
        os.path.exists(TEMPORARY_IMAGE[1:])
        os.remove(TEMPORARY_IMAGE[1:])


    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    pil = Pil.open(image_url[1:]) # remove first / from image url

    SIZE_NOW = pil.size
    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': pil.size[0],
        'image_height': pil.size[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }

    return render(request, 'tugas_dua/image.html', context)

def viewZoomOutImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")
    
    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:]) # remove first / from image url

    if(SIZE_NOW[0]//2 > 1 and SIZE_NOW[1]//2 > 1):
        resize = (SIZE_NOW[0]//2, SIZE_NOW[1]//2)
        pil = pil.resize(resize)
        image_url = TEMPORARY_IMAGE
        pil.save(image_url[1:])
        SIZE_NOW = pil.size
    else: return redirect('/image/view/'+id)
    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': SIZE_NOW[0],
        'image_height': SIZE_NOW[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewZoomInImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    # if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url

    if (SIZE_NOW[0] * 2 < 10000 and SIZE_NOW[1] * 2 < 10000):
        resize = (SIZE_NOW[0] * 2, SIZE_NOW[1] * 2)
        pil = pil.resize(resize)
        image_url = TEMPORARY_IMAGE
        pil.save(image_url[1:])
        SIZE_NOW = pil.size
    else: return redirect('/image/view/' + id)

    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': SIZE_NOW[0],
        'image_height': SIZE_NOW[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewFlipVerticalImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.transpose(Pil.FLIP_LEFT_RIGHT)
    image_url = TEMPORARY_IMAGE
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': SIZE_NOW[0],
        'image_height': SIZE_NOW[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewFlipHorizontalImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.transpose(Pil.FLIP_TOP_BOTTOM)
    image_url = TEMPORARY_IMAGE
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': SIZE_NOW[0],
        'image_height': SIZE_NOW[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewRotateImage(request, id, degree):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/tmp/"): os.mkdir("static/tmp/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.rotate(int(degree))
    image_url = TEMPORARY_IMAGE
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': SIZE_NOW[0],
        'image_height': SIZE_NOW[1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)
