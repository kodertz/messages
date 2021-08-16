from django.db.models import fields
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
class HomePage(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html' 
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'text']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
    
