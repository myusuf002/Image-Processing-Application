from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
<<<<<<< HEAD
from PIL import Image as Pil
import os
SIZE_NOW = (0, 0)
TEMPORARY_IMAGE = "/assets/temporary_image.jpg"
=======
from PIL import Image as Pil, ImageOps
import matplotlib.pyplot as plt

import os
import numpy as np
SIZE_NOW = (0, 0)
TEMPORARY_IMAGE = "/assets/temporary_image.jpeg"
>>>>>>> Histogram & Color Transform

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

<<<<<<< HEAD

=======
>>>>>>> Histogram & Color Transform
def viewImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")
    
    if os.path.exists(TEMPORARY_IMAGE[1:]):
        os.path.exists(TEMPORARY_IMAGE[1:])
        os.remove(TEMPORARY_IMAGE[1:])


    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    pil = Pil.open(image_url[1:]) # remove first / from image url
<<<<<<< HEAD

=======
	
>>>>>>> Histogram & Color Transform
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
    if not os.path.exists("static/"): os.mkdir("static/")
    
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
    if not os.path.exists("static/"): os.mkdir("static/")

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
    if not os.path.exists("static/"): os.mkdir("static/")

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
    if not os.path.exists("static/"): os.mkdir("static/")

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
    if not os.path.exists("static/"): os.mkdir("static/")

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
<<<<<<< HEAD
=======
    
def viewCropImage(request, id, left, top, right, bottom):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url
    crop_size = (int(left), int(top), int(right), int(bottom))
    pil = pil.crop(crop_size)
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

def viewCutImage(request, id, left, top, right, bottom, x, y):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:])  # remove first / from image url
    cut_size = (int(left), int(top), int(right), int(bottom))
    cut_pil = pil.crop(cut_size)
    
    width = int(right) - int(left)
    height = int(bottom) - int(top)
    blank_arr = np.zeros((height, width, 3), dtype=np.uint8)
    blank_pil = Pil.fromarray(blank_arr, 'RGB')
    pil.paste(blank_pil, (int(left), int(top)))
	
    paste_dst = (int(x), int(y))
    pil.paste(cut_pil, paste_dst)
    
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
    
def viewRGBImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:]).convert("RGB")  # remove first / from image url
    
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

def viewHSVImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:]).convert("HSV")  # remove first / from image url
    
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

def viewGrayImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(TEMPORARY_IMAGE[1:]): image_url = TEMPORARY_IMAGE
    pil = Pil.open(image_url[1:]).convert("L")   # remove first / from image url
    
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

def viewHistogramImage(request, id):
    global SIZE_NOW
    global TEMPORARY_IMAGE
    if not os.path.exists("static/"): os.mkdir("static/")
    
    if os.path.exists(TEMPORARY_IMAGE[1:]):
        os.path.exists(TEMPORARY_IMAGE[1:])
        os.remove(TEMPORARY_IMAGE[1:])


    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    pil = Pil.open(image_url[1:]) # remove first / from image url
   
    hs = pil.histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    # ax.axis([0, 255, 0, max(hs)])
    red_url = "/assets/temporary_red_"+id+".jpeg"
    fig.savefig(red_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    # ax.axis([0, 255, 0, max(hs)])
    green_url = "/assets/temporary_green_"+id+".jpeg"
    fig.savefig(green_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    # ax.axis([0, 255, 0, max(hs)])
    blue_url = "/assets/temporary_blue_"+id+".jpeg"
    fig.savefig(blue_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    rgb_url = "/assets/temporary_rgb_"+id+".jpeg"
    fig.savefig(rgb_url[1:])
    
    hs = pil.convert("L").histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(len(hs)), hs, color='gray')
    # ax.axis([0, 255, 0, max(hs)])
    gray_url = "/assets/temporary_gray_"+id+".jpeg"
    fig.savefig(gray_url[1:])
    
    eq = ImageOps.equalize(pil)
    hs = eq.histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    eq_url = "/assets/temporary_eq_"+id+".jpeg"
    fig.savefig(eq_url[1:])
    
    SIZE_NOW = pil.size
    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'red_url': red_url,
        'green_url': green_url,
        'blue_url': blue_url,
        'rgb_url': rgb_url,
        'gray_url': gray_url,
        'eq_url': eq_url,
        
    }

    return render(request, 'tugas_dua/histogram.html', context)
>>>>>>> Histogram & Color Transform
