from django.shortcuts import render
from django.http import HttpResponse

# VIEWS
def welcome(request):
    return HttpResponse('welcome to snaps app')


