from django.shortcuts import render
from django.views.generic import ListView

from .models import Send
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm

class HomePageView(ListView):
    model = Send
    template_name = "home.html"
# Create your views here.



#...
