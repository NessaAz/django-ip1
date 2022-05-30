from django.urls import re_path as path
from .views import PhotoListView, PhotoDetailView, PhotoTagListView

app_name = 'snaps'

urlpatterns = [ 
    path('', PhotoListView.as_view(), name='list'),
    path('tag/<slug:tag>/', PhotoTagListView.as_view(), name='tag'),
    path('snaps/<int:pk>/', PhotoDetailView.as_view(), name='detail'),
]

