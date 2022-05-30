from django.urls import re_path as url, path
from . import views
from .views import PhotoListView, PhotoDetailView, PhotoTagListView

urlpatterns = [
    #url(r"", views.welcome, name="welcome"),    
    path('', PhotoListView.as_view(), name='list')
]

