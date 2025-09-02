# I Have Created This FILE - Arpit Katiyar
from django.http import HttpResponse
from django.shortcuts import render


def home(request) :
    return HttpResponse('''HOME!''')

def removepunc(request) :
    return HttpResponse('''REMOVE!''')

def capfirst(request) :
    return HttpResponse('''CAP FIRST''')

def newlineremove(request) :
    return HttpResponse('''NEWLINE REMOVE!''')

def spaceremove(request) :
    return HttpResponse('''SPACE REMOVE!''')

def charcount(request) :
    return HttpResponse('''CHARACTER COUNT!''')

