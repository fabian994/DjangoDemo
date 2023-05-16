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
    # sourcery skip: hoist-statement-from-if, remove-redundant-pass
    print(request)
    if request.method == "POST":
        print("enter post")
        c_relForm = cRelDBf(request.POST)
        context = {"title": "Registro de usuarios", "form": c_relForm}
        #print(c_relForm)
        if c_relForm.is_valid():
            print("FORM VALID!")

            data = c_relForm.cleaned_data

            print("data:\n", data)
            #Checks if key does not already exists in DB
            if Student.objects.filter(matricula=data["matricula"]).exists():
                print("Matricula existe")
                messages.error(request, "Este correo ya fue usado")
            try:
                #Creates records in table
                Student.objects.create(
                    matricula=data["matricula"],
                    name=data["name"],
                    age=data["age"],
                )

                messages.success(request, "Datos guardados correctamente")
                print("create success")

                return redirect("home")
            
            except Exception:
                print("create failed")
                messages.error(request, "Error al guardar los datos")
        else:
            #print(c_relForm.errors.as_data())
            print('form no valid')
            return render(request, "writeRel.html", context)
        return render(request, "writeRel.html", context)

    else:
        print("no post")
        c_relForm = cRelDBf()
        context = {"title": "Registro de Usuarios", "form": c_relForm}

        return render(request, "writeRel.html", context)
    pass

def c_NOrel():
    pass

def r_rel(request):
        lista_all = models.Student.objects.all()
        student_get = models.Student.objects.get(age='21') 
        lista_filter = models.Student.objects.filter(age='22')       
        return render(request, 'readRelDB.html', {'li_all': lista_all, 'student_get': student_get, "li_filter": lista_filter})
        
def r_NOrel():
    pass