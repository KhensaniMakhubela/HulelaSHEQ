from django.shortcuts import render
from django.http import HttpResponse
from .models import MainMenu

def home(request):

    menu_list = MainMenu.objects.all()

    context = {'menu_list': menu_list}

    return render(request, "Menu_Site.html" , context)
