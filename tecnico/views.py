from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from tecnico.models import Tecnico

class TecnicoListView(ListView):
    model = Tecnico
    template_name = "tecnico/tecnico_list.html"


class TecnicoDetailView(DetailView):
    model = Tecnico
    template_name = "tecnico/tecnico_detail.html"


class TecnicoCreateView(LoginRequiredMixin, CreateView):
    model = Tecnico
    success_url = reverse_lazy('tecnico:tecnico-list')
    fields = '__all__'


class TecnicoUpdateView(LoginRequiredMixin, UpdateView):
    model = Tecnico
    success_url = reverse_lazy('tecnico:tecnico-list')
    fields = '__all__'


class TecnicoDeleteView(LoginRequiredMixin, DeleteView):
    model = Tecnico
    success_url = reverse_lazy('tecnico:tecnico-list')