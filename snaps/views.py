from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Photo


class PhotoListView(ListView):    
    model = Photo     
    template_name = 'snaps/list.html'
    context_object_name = 'photos'    

class PhotoTagListView(PhotoListView):    
    template_name = 'snaps/taglist.html'

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
    context_object_name = 'snaps'    