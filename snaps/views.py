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

class PhotoTagListView(PhotoListView):    
    template_name = 'photoapp/taglist.html'

    # Custom method
    def get_tag(self):
        return self.kwargs.get('tag')

    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context
    
class PhotoDetailView(DetailView):    
    model = Photo
    template_name = 'snaps/detail.html'
    context_object_name = 'photo'    