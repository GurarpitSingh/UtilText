# I have created this file - Guri
import fileinput

from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def about(request):
    return HttpResponse('''<h1> <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">link lelo ji</a></h1>''')
def ex1(request):

    return HttpResponse('<h1>Welcome To Navigator</h1><br><p><a href="https://www.google.com/">Google</a></p><br><p><a href="https://www.facebook.com/">Facebook</a></p>')


def analyze(request):
    textdj = (request.POST.get('text', 'default'))
    removepunc = (request.POST.get('removepunc', 'off'))
    uppercase = (request.POST.get('uppercase', 'off'))

    extraspaceremove = (request.POST.get('extraspaceremove', 'off'))
    # print(textdj)
    # print(removepunc)
    punctuations = ''' !"#$%&'()*+, -./:;<=>?@[\]^_`{|}~ '''
    analyzed = ''






    if(removepunc == 'on'):
        analyzed=''
        for char in textdj:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': '', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        textdj= analyzed
    if(uppercase == 'on'):
        analyzed = ''
        for char in textdj:
            analyzed = analyzed + char.upper()
        params = {'purpose': '', 'analyzed_text': analyzed}
        textdj = analyzed

    if (extraspaceremove == 'on'):
        analyzed=''
        for index, char in enumerate(textdj):
            if not (textdj[index] == ' ' and textdj[index+1] == ' '):

                analyzed = analyzed + char
        params = {'purpose': '', 'analyzed_text': analyzed}

    if(removepunc != 'on' and uppercase !='on' and extraspaceremove != 'on'):
        # params = {'Nothing To Display': 'Null'}
        return HttpResponse("Error")



    return render(request, 'analyze.html', params)









def spacer(request):
    return HttpResponse("hello Guri")


def removepunc(request):
    return HttpResponse("hello Guri")


def capitalize(request):
    return HttpResponse("hello Guri")

def spaceremove(request):
    return HttpResponse("hello Guri")