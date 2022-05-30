from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Photo
from django.http import HttpResponse

# VIEWS
def welcome(request):
    return HttpResponse('welcome to snaps app')

class PhotoListView(ListView):    
    model = Photo     
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'

