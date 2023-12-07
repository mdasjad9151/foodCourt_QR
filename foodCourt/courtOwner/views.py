from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .forms import UserRegisterForm, AddFoodCourt
from .models import Owner

# Qr code module 
import qrcode
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your views here.

def sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/owner/profile/')
        # return HttpResponse("user hai")
    else:
        if request.method == 'POST':
            fm = UserRegisterForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/owner/login/')
        else:
         fm = UserRegisterForm()
    return render(request,  'courtOwner/signup.html',{'from': fm})

def log_in(request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/owner/profile/')
        else:
            if request.method == 'POST':
                fm = AuthenticationForm(request= request, data=request.POST)
                if fm.is_valid():
                    uname = fm.cleaned_data['username']
                    upwd = fm.cleaned_data['password']
                    user_auth = authenticate(username = uname, password = upwd)
                    if user_auth is not None:
                        login(request, user_auth)
                        return HttpResponseRedirect('/owner/login/')
            else:
                fm = AuthenticationForm()
        return render(request, 'courtOwner/login.html', {'form': fm})

def user_profile(request):
    if request.user.is_authenticated is None:
        
        return HttpResponseRedirect('/owner/login/')
    return render(request, 'courtOwner/profile.html')

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/owner/login/') 


# QR code generater Functions

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def save_qr_code_image(data):
    img = generate_qr_code(data)
    img_io = BytesIO()
    img.save(img_io, format='PNG')
    return SimpleUploadedFile(f"qrcode_{data}.png", img_io.getvalue(), content_type="image/png")


# main features

def addFoodCourt(request):
    if request.method ==  'POST':
        fm =  AddFoodCourt(request.POST)
        if fm.is_valid():
            your_data = fm.cleaned_data['name']
            qr_code_image = save_qr_code_image(your_data)
            qr_code_image_instance = Owner.objects.create(qr=qr_code_image)
            # The ID of the instance will be used as the name of the QR code image.
            qr_code_image_instance.qr.name = f'qrcodes/{qr_code_image_instance.id}.png'
            qr_code_image_instance.save()
            fm.save()
    fm  = AddFoodCourt()
    return render(request, 'courtOwner/courtInfo.html', {'form': fm})
