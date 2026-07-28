from django.views.generic import ListView, CreateView, DetailView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_single.html'

class PostNewView(CreateView):
    model = Post
    template_name = 'post_new.html'
    form_class = PostForm
    success_url = reverse_lazy('home')