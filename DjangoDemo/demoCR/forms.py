from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
from .models import *
from django.core import validators
from django.core.validators import RegexValidator

letras = RegexValidator(r'^[a-zA-Z " " éáíóúñÑÁÉÍÓÚ]*$', 'Solo se pueden ingresar letras ')
numeros = RegexValidator(r'^[0-9]*$', 'Solo se pueden ingresar numeros')
matricula = RegexValidator(r'^[a-zA-Z0-9]*$', 'Solo se pueden ingresar numeros y letras')

class cRelDBf(forms.Form):
    matricula = forms.CharField( max_length = 10, 
                            required = True, 
                            label = "Matricula",
                            validators=[matricula],
                            error_messages={
                                "required": "No puede estar vacío",
                            },
                            widget = forms.TextInput(attrs = {
                                "class": "form-control"
                                }
                            ))

    name = forms.CharField( max_length = 38, 
                                required = True,
                                label = "Nombre",
                                validators=[letras],
                                error_messages={
                                    "required": "No puede estar vacío",
                                },
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    age = forms.IntegerField(    max_value=100,
                                        required = True, 
                                        label = "Codigo Postal",
                                        validators=[numeros],
                                        error_messages={
                                            "required": "No puede estar vacío",
                                        },
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                            }
                                        ))
    
class cNonRelDBf(forms.Form):
    matricula = forms.CharField( max_length = 10, 
                            required = True, 
                            label = "Matricula",
                            validators=[matricula],
                            error_messages={
                                "required": "No puede estar vacío",
                            },
                            widget = forms.TextInput(attrs = {
                                "class": "form-control"
                                }
                            ))

    name = forms.CharField( max_length = 38, 
                                required = True,
                                label = "Nombre",
                                validators=[letras],
                                error_messages={
                                    "required": "No puede estar vacío",
                                },
                                widget = forms.TextInput(attrs = {
                                    "class": "form-control"
                                    }
                                ))

    age = forms.IntegerField(    max_value=100,
                                        required = True, 
                                        label = "Codigo Postal",
                                        validators=[numeros],
                                        error_messages={
                                            "required": "No puede estar vacío",
                                        },
                                        widget = forms.TextInput(attrs = {
                                            "class": "form-control"
                                            }
                                        ))