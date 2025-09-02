# I Have Created This FILE - Arpit Katiyar
from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    return HttpResponse('''<h1>Hello, World!</h1>Home<br><a href="https://www.codewithharry.com/">Harry's Website</a>''')