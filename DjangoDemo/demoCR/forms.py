from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.hashers import check_password
import datetime
from django.contrib import messages
from .models import *
from django.core import validators
from django.core.validators import RegexValidator