from django.shortcuts import render
from django.contrib.auth import logout, login
from django.http import FileResponse, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from django.forms import formset_factory
from bson import ObjectId
from datetime import datetime
import string
import random

from .forms import *
from .models import *
# Create your views here.


def home(request, *args, **kwargs):
    print(request)
    # return render(request, "registration/login.html")
    # #return HttpResponse("<h1>Hello World</h1>")
    # if request.user.is_authenticated:
    #     return render(request, "census/home.html")

    return render(request,"home.html")

def c_rel():
    pass

def c_NOrel():
    pass
def r_rel():
    pass
def r_NOrel():
    pass