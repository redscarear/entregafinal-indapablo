from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from productor.models import Productor

class ProductorListView(ListView):
    model = Productor
    template_name = "productor/productor_list.html"


class ProductorDetailView(DetailView):
    model = Productor
    template_name = "productor/productor_detail.html"


class ProductorCreateView(LoginRequiredMixin, CreateView):
    model = Productor
    success_url = reverse_lazy('productor:productor-list')
    fields = '__all__'


class ProductorUpdateView(LoginRequiredMixin, UpdateView):
    model = Productor
    success_url = reverse_lazy('productor:productor-list')
    fields = '__all__'


class ProductorDeleteView(LoginRequiredMixin, DeleteView):
    model = Productor
    success_url = reverse_lazy('productor:productor-list')
