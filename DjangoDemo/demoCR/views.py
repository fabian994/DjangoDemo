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

def c_rel(request):
    print(request)
    if request.method == "POST":
        print("enter post")
        c_relForm = cRelDBf(request.POST)
        context = {"title": "Registro de usuarios", "form": c_relForm}

        if c_relForm.is_valid():
            print("FORM VALID!")

            data = c_relForm.cleaned_data

            print("data:\n", data)
            #m = data["email"]
            # print(usuario.objects.filter(mail="a01360000@tec.mx"))
            if Student.objects.filter(matricula=data["matricula"]).exists():
                print("Matricula existe")
                messages.error(request, "Este correo ya fue usado")
            else:
                print("no existe")
                try:
                    print("create success")

                    Student.objects.create(
                        # id = unique_id(8),
                        matricula=data["matricula"],
                        name=data["name"],
                        age=data["age"],
                    )

                    messages.success(request, "Datos guardados correctamente")

                    return redirect("login")

                except:
                    print("creare failed")
                    messages.error(request, "Error al guardar los datos")

        return render(request, "writeRel.html", context)

    else:
        print("no post")
        c_relForm = cRelDBf()
        context = {"title": "Registro de Usuarios", "form": c_relForm}

        return render(request, "writeRel.html", context)
    pass

def c_NOrel():
    pass
def r_rel():
    pass
def r_NOrel():
    pass