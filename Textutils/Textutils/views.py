# I Have Created This FILE - Arpit Katiyar
from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    return render(request, 'home.html')
    # return HttpResponse('''HOME!
    # <h3><a href="/">Back</a></h3>
    # ''')

def removepunc(request) :
    return HttpResponse('''REMOVE!
    <h3><a href="/">Back</a></h3>
    ''')

def capfirst(request) :
    return HttpResponse('''CAP FIRST
    <h3><a href="/">Back</a></h3>
    ''')

def newlineremove(request) :
    return HttpResponse('''NEWLINE REMOVE!
    <h3><a href="/">Back</a></h3>
    ''')

def spaceremove(request) :
    return HttpResponse('''SPACE REMOVE!
    <h3><a href="/">Back</a></h3>
    ''')

def charcount(request) :
    return HttpResponse('''
    CHARACTER COUNT!
    <h3><a href="/">Back</a></h3>
    ''')

