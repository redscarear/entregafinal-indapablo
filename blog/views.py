from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"
    fields = ['title', 'author', 'content']


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')
    fields = ['title', 'author', 'content']


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')
    fields = ['title', 'author', 'content']


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog-list')

		
