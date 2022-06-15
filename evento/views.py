from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from evento.models import Evento

class EventoListView(ListView):
    model = Evento
    template_name = "evento/evento_list.html"


class EventoDetailView(DetailView):
    model = Evento
    template_name = "evento/evento_detail.html"
    fields = ['name', 'code', 'description']


class EventoCreateView(LoginRequiredMixin, CreateView):
    model = Evento
    success_url = reverse_lazy('evento:evento-list')
    fields = ['name', 'code', 'description']


class EventoUpdateView(LoginRequiredMixin, UpdateView):
    model = Evento
    success_url = reverse_lazy('evento:evento-list')
    fields = ['name', 'code', 'description']


class EventoDeleteView(LoginRequiredMixin, DeleteView):
    model = Evento
    success_url = reverse_lazy('evento:evento-list')

		
