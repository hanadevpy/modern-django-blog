from django.urls import path
from .views import (
    HomeView, 
    PostNewView,
    PostDetailView
)

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('post/new', PostNewView.as_view() , name='post_new'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
]