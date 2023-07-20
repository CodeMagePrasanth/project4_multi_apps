from django.shortcuts import render

from django.http import HttpResponse

def string1_response_app1(request):
    return HttpResponse('<marquee><h1>This is my first String respose app1</h1></marquee>')

def string2_response_app2(request):
    return HttpResponse('<marquee><h1>This is my first String respose app2</h1></marquee>')

def string3_response_app3(request):
    return HttpResponse('<marquee><h1>This is my first String respose app3</h1></marquee>')
