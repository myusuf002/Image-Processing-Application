from django.shortcuts import render, get_object_or_404, redirect
from .models import Image
from .forms import ImageForm
from PIL import Image as Pil, ImageOps
import matplotlib.pyplot as plt

import os
import glob

import numpy as np
import datetime

# Create your views here.
def viewIndex(request):
    if 'code' in request.session: 
        temp = request.session['code']
        # del request.session['code']
        my_dir = "./assets/"
        for fname in os.listdir(my_dir):
            if fname.startswith(temp):
                print(fname)
                os.remove(os.path.join(my_dir, fname)) 

    if 'temporary' in request.session: del request.session['temporary']
    if 'size' in request.session: del request.session['size']

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
    if 'code' in request.session: 
        temp = request.session['code']
        # del request.session['code']
        my_dir = "./assets/"
        for fname in os.listdir(my_dir):
            if fname.startswith(temp):
                print(fname)
                os.remove(os.path.join(my_dir, fname)) 

    if 'temporary' in request.session: del request.session['temporary']
    if 'size' in request.session: del request.session['size']

    code = str(datetime.datetime.now()).replace(':', '-').replace('.', '-') 
    request.session['code'] = code
    request.session['temporary'] = "/assets/" + code + ".jpeg"
    print("new", code)

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    pil = Pil.open(image_url[1:]) # remove first / from image url
	
    request.session['size'] = pil.size
    
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
    if not os.path.exists("static/"): os.mkdir("static/")
    
    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]) # remove first / from image url

    if(request.session['size'][0]//2 > 1 and request.session['size'][1]//2 > 1):
        resize = (request.session['size'][0]//2, request.session['size'][1]//2)
        pil = pil.resize(resize)
        image_url = request.session['temporary']
        pil.save(image_url[1:])
        request.session['size'] = pil.size
    else: return redirect('/image/view/'+id)
    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewZoomInImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:])  # remove first / from image url

    if (request.session['size'][0] * 2 < 10000 and request.session['size'][1] * 2 < 10000):
        resize = (request.session['size'][0] * 2, request.session['size'][1] * 2)
        pil = pil.resize(resize)
        image_url = request.session['temporary']
        pil.save(image_url[1:])
        request.session['size'] = pil.size
    else: return redirect('/image/view/' + id)

    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewFlipVerticalImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.transpose(Pil.FLIP_LEFT_RIGHT)
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewFlipHorizontalImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.transpose(Pil.FLIP_TOP_BOTTOM)
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewRotateImage(request, id, degree):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:])  # remove first / from image url
    pil = pil.rotate(int(degree))
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)
    
def viewCropImage(request, id, left, top, right, bottom):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:])  # remove first / from image url
    crop_size = (int(left), int(top), int(right), int(bottom))
    pil = pil.crop(crop_size)
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewCutImage(request, id, left, top, right, bottom, x, y):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
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
    
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)
    
def viewRGBImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]).convert("RGB")  # remove first / from image url
    
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewHSVImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]).convert("HSV")  # remove first / from image url
    
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewGrayImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]).convert("L")   # remove first / from image url
    
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)

def viewHistogramImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")
    
    if os.path.exists(request.session['temporary'][1:]):
        os.path.exists(request.session['temporary'][1:])
        os.remove(request.session['temporary'][1:])


    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    pil = Pil.open(image_url[1:]) # remove first / from image url
   
    hs = pil.histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    # ax.axis([0, 255, 0, max(hs)])
    red_url = "/assets/"+request.session['code']+"_red.jpeg"
    fig.savefig(red_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    # ax.axis([0, 255, 0, max(hs)])
    green_url = "/assets/"+request.session['code']+"_green.jpeg"
    fig.savefig(green_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    # ax.axis([0, 255, 0, max(hs)])
    blue_url = "/assets/"+request.session['code']+"_blue.jpeg"
    fig.savefig(blue_url[1:])
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    rgb_url = "/assets/"+request.session['code']+"_rgb.jpeg"
    fig.savefig(rgb_url[1:])
    
    hs = pil.convert("L").histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(len(hs)), hs, color='gray')
    # ax.axis([0, 255, 0, max(hs)])
    gray_url = "/assets/"+request.session['code']+"_gray.jpeg"
    fig.savefig(gray_url[1:])
    
    eq = ImageOps.equalize(pil)
    hs = eq.histogram()
    
    fig, ax = plt.subplots()
    ax.bar(range(256), hs[:256], color='r', alpha=0.5)
    ax.bar(range(256), hs[:256:2*256], color='g', alpha=0.4)
    ax.bar(range(256), hs[2*256:], color='b', alpha=0.3)
    eq_url = "/assets/"+request.session['code']+"_eq.jpeg"
    fig.savefig(eq_url[1:])
    
    request.session['size'] = pil.size
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



# Open an Image
def open_image(path):
    newImage = Pil.open(path)
    return newImage

# Save Image
def save_image(image, path):
    Pil.save(path, 'png')

# Create a new image with the given size
def create_image(i, j):
    image = Pil.new("RGB", (i, j), "white")
    return image

# Get the pixel from the given image
def get_pixel(image, i, j):

    # Inside image bounds?
    width, height = image.size
    if i > width or j > height:
        return None

    # Get Pixel
    pixel = image.getpixel((i, j))
    return pixel

# Create a Half-tone version of the image
def convert_halftoning(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Transform to half tones
    for i in range(0, width, 2):
        for j in range(0, height, 2):
            # Get Pixels
            p1 = get_pixel(image, i, j)
            p2 = get_pixel(image, i, j + 1)
            p3 = get_pixel(image, i + 1, j)
            p4 = get_pixel(image, i + 1, j + 1)

            # Transform to grayscale
            gray1 = (p1[0] * 0.299) + (p1[1] * 0.587) + (p1[2] * 0.114)
            gray2 = (p2[0] * 0.299) + (p2[1] * 0.587) + (p2[2] * 0.114)
            gray3 = (p3[0] * 0.299) + (p3[1] * 0.587) + (p3[2] * 0.114)
            gray4 = (p4[0] * 0.299) + (p4[1] * 0.587) + (p4[2] * 0.114)

            # Saturation Percentage
            sat = (gray1 + gray2 + gray3 + gray4) / 4

            # Draw white/black depending on saturation
            if sat > 223:
                pixels[i, j]         = (255, 255, 255) # White
                pixels[i, j + 1]     = (255, 255, 255) # White
                pixels[i + 1, j]     = (255, 255, 255) # White
                pixels[i + 1, j + 1] = (255, 255, 255) # White
            elif sat > 159:
                pixels[i, j]         = (255, 255, 255) # White
                pixels[i, j + 1]     = (0, 0, 0)       # Black
                pixels[i + 1, j]     = (255, 255, 255) # White
                pixels[i + 1, j + 1] = (255, 255, 255) # White
            elif sat > 95:
                pixels[i, j]         = (255, 255, 255) # White
                pixels[i, j + 1]     = (0, 0, 0)       # Black
                pixels[i + 1, j]     = (0, 0, 0)       # Black
                pixels[i + 1, j + 1] = (255, 255, 255) # White
            elif sat > 32:
                pixels[i, j]         = (0, 0, 0)       # Black
                pixels[i, j + 1]     = (255, 255, 255) # White
                pixels[i + 1, j]     = (0, 0, 0)       # Black
                pixels[i + 1, j + 1] = (0, 0, 0)       # Black
            else:
                pixels[i, j]         = (0, 0, 0)       # Black
                pixels[i, j + 1]     = (0, 0, 0)       # Black
                pixels[i + 1, j]     = (0, 0, 0)       # Black
                pixels[i + 1, j + 1] = (0, 0, 0)       # Black

    # Return new image
    return new

def viewHalftoningImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]) # remove first / from image url
    
    # Convert to Halftoning and save
    pil = convert_halftoning(pil)
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)


# Return color value depending on quadrant and saturation
def get_saturation(value, quadrant):
    if value > 223: return 255
    elif value > 159:
        if quadrant != 1: return 255
        return 0

    elif value > 95:
        if quadrant == 0 or quadrant == 3: return 255
        return 0
    elif value > 32:
        if quadrant == 1: return 255
        return 0
    else: return 0

# Create a dithered version of the image
def convert_dithering(image):
    # Get size
    width, height = image.size

    # Create new Image and a Pixel Map
    new = create_image(width, height)
    pixels = new.load()

    # Transform to half tones
    for i in range(0, width, 2):
        for j in range(0, height, 2):
            # Get Pixels
            p1 = get_pixel(image, i, j)
            p2 = get_pixel(image, i, j + 1)
            p3 = get_pixel(image, i + 1, j)
            p4 = get_pixel(image, i + 1, j + 1)

            # Color Saturation by RGB channel
            red   = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
            green = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
            blue  = (p1[2] + p2[2] + p3[2] + p4[2]) / 4

            # Results by channel
            r = [0, 0, 0, 0]
            g = [0, 0, 0, 0]
            b = [0, 0, 0, 0]

            # Get Quadrant Color
            for x in range(0, 4):
                r[x] = get_saturation(red, x)
                g[x] = get_saturation(green, x)
                b[x] = get_saturation(blue, x)

                # Set Dithered Colors
                pixels[i, j]         = (r[0], g[0], b[0])
                pixels[i, j + 1]     = (r[1], g[1], b[1])
                pixels[i + 1, j]     = (r[2], g[2], b[2])
                pixels[i + 1, j + 1] = (r[3], g[3], b[3])

    # Return new image
    return new

def viewDitheringImage(request, id):
    if not os.path.exists("static/"): os.mkdir("static/")

    image = get_object_or_404(Image, pk=id)
    image_url = image.image.url
    image_name = image.image.url[len("/image/img/"):]
    if os.path.exists(request.session['temporary'][1:]): image_url = request.session['temporary']
    pil = Pil.open(image_url[1:]) # remove first / from image url
    
    # Convert to Halftoning and save
    pil = convert_dithering(pil)
    image_url = request.session['temporary']
    pil.save(image_url[1:])


    context = {
        'title': "Tugas Dua",
        'image_id': image.id,
        'image_url': image_url,
        'image_name': image_name,
        'image_width': request.session['size'][0],
        'image_height': request.session['size'][1],
        'image_format': pil.format,
        'image_mode': pil.mode,
    }
    return render(request, 'tugas_dua/image.html', context)



