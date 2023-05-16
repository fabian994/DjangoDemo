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

import utils

from .forms import *
from .models import *
# Create your views here.

db = utils.get_db_handle("formDB")


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
        
            print("no existe")
            try:
                
                Student.objects.create(
                    # id = unique_id(8),
                    matricula=data["matricula"],
                    name=data["name"],
                    age=data["age"],
                )

                messages.success(request, "Datos guardados correctamente")
                print("create success")

                return redirect("login")
            
            except Exception:
                print("creare failed")
                messages.error(request, "Error al guardar los datos")

        return render(request, "writeRel.html", context)

    else:
        print("no post")
        c_relForm = cRelDBf()
        context = {"title": "Registro de Usuarios", "form": c_relForm}

        return render(request, "writeRel.html", context)
    pass

def c_NOrel(request):
    
    form = cNonRelDBf()
    context = {
        "form" : form,
        "title" : "Registro de usuarios"
    }

    if request.method == "POST":
        
        form = cNonRelDBf(request.POST)
        context = {
            "form" : form,
            "title" : "Registro de usuarios"
        }
        
        print("enter post")
        print(form.is_valid())
        print(form.errors)
        
        if form.is_valid():
            print("FORM VALID!")

            data = form.cleaned_data

            if db.users.find_one({"matricula": data["matricula"]}):
                print("Matricula existe")
                messages.error(request, "Esta matricula ya fue usada")
                return render(request,"writeNonRel.html", context)

            try: 
                db.users.insert_one({
                    "matricula" : data["matricula"],
                    "name" : data["name"],
                    "age" : data["age"]
                })

                print("create success")
                messages.success(request, "Datos guardados correctamente")
                return redirect("c-norel")

            except Exception as e:
                print("create failed")
                messages.error(request, f"Error al guardar los datos: {e}")
                return render(request,"writeNonRel.html", context)

        return render(request,"writeNonRel.html", context)

    return render(request,"writeNonRel.html", context)
    
    
def r_rel():
    pass
def r_NOrel():
    pass