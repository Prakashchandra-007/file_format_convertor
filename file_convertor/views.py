
from django.shortcuts import render
from file_convertor.forms import UserProfileInfoForm, UserForm
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .forms import UploadFileForm

import mimetypes
import os


def index(request):
    return render(request, 'index.html')


def main_page(request):
    return render(request, 'main_page.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                registered = True
            else:
                print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'registrations.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('file_convertor:main_page'))
            else:
                return HttpResponse("account not active")
        else:
            print("some tried to login and field")
            print("username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('file_convertor:index'))


@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():

            handle_uploaded_file(request.FILES['file'])

            return HttpResponseRedirect('landing')
    else:
        form = UploadFileForm()
    return render(request, 'main_page.html', {'form': form})


def handle_uploaded_file(f):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    with open(BASE_DIR + '/static/upload/download.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def conver(request):
    print("working>>>>>>>>>>>>>>>>")
    return HttpRespons('final tuns')
#  download file


def download_page(request):

    return render(request, 'download.html')


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'test.txt'
    # Define the full file path

    filepath = BASE_DIR + '/static/upload/' + filename

    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
