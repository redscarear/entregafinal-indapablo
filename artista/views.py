from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from artista.models import Artista

class ArtistaListView(ListView):
    model = Artista
    template_name = "artista/artista_list.html"


class ArtistaDetailView(DetailView):
    model = Artista
    template_name = "artista/artista_detail.html"


class ArtistaCreateView(LoginRequiredMixin, CreateView):
    model = Artista
    success_url = reverse_lazy('artista:artista-list')
    fields = '__all__'


class ArtistaUpdateView(LoginRequiredMixin, UpdateView):
    model = Artista
    success_url = reverse_lazy('artista:artista-list')
    fields = '__all__'


class ArtistaDeleteView(LoginRequiredMixin, DeleteView):
    model = Artista
    success_url = reverse_lazy('artista:artista-list')
# Create your views here.
