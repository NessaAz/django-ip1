from django.urls import re_path as url, path
from . import views
from .views import PhotoListView, PhotoDetailView, PhotoTagListView

urlpatterns = [
    #url("", views.welcome, name="welcome"),    
    path('', PhotoListView.as_view(), name='list'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
]

