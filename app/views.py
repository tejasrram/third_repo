from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def string_response(request):
    return HttpResponse('this the first string')

def string_two(request):
    return HttpResponse('this is the second string') 

def string_three(request):
    return HttpResponse('the third string ')