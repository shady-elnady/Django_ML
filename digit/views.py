from django.http import HttpResponse
from django.shortcuts import render, redirect

from digit.api.serializer import Base64ImageField, DigitSerializer

from .forms import *
import re
import base64
from PIL import Image
import io
from django.core.files.storage import FileSystemStorage
from .models import Digit


def home_view(request):
    return render(request, 'home.html')


# Create your views here.
def digit_image_view(request):
  
    if request.method == 'POST':
        form = DigitForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DigitForm()
    return render(request, 'digit_image_form.html', {'form' : form})
  
  
def success(request):
    return HttpResponse('successfully uploaded')
  
def display_digit_images(request):
  
  if request.method == 'GET':

    # getting all the objects of hotel.
    digits = Digit.objects.all() 
    return render(request, 'display_digit_images.html', {'digit_images' : digits})


# for Django Templates
def canvas_image(request):
    if request.method=="POST":
        # print("-------",request.POST)
        if request.POST.get('captured_image'):
            captured_image = request.POST.get('captured_image')
            # imgstr = captured_image.decode('base64')
            # print("image 1: --------------------------------------", captured_image)
            # imgstr = re.search('base64,(.*)', captured_image).group(1)
            # print("image 2: --------------------------------------", imgstr)
            # imgstr = base64.b64decode(imgstr)
            # print("image 3: --------------------------------------", imgstr)
            # tempimg = io.BytesIO(imgstr)
            # im = Image.open(tempimg)
            # im.show()
            captured_image = Base64ImageField.to_internal_value(Base64ImageField(),captured_image)
            img = Digit()
            img.image = captured_image
            result = img.save()
            return render(request, 'canvas.html', {'result' : result})
            
    return render(request, 'canvas.html', {'title' : 'Digit Classify'})

# for Upload Files
def upload(request):
    if request.method == 'POST' and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        return render(request, 'main/upload.html', {'file_url': file_url})
    return render(request, 'main/upload.html')
