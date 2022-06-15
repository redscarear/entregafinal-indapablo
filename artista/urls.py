from django.urls import path
from artista import views
app_name='artista'
urlpatterns = [
    			path('artista', views.ArtistaListView.as_view(), name='artista-list'),
    			path('artista/add/', views.ArtistaCreateView.as_view(), name='artista-add'),
    			path('artista/<int:pk>/detail', views.ArtistaDetailView.as_view(), name='artista-detail'),
    			path('artista/<int:pk>/update', views.ArtistaUpdateView.as_view(), name='artista-update'),
    			path('artista/<int:pk>/delete', views.ArtistaDeleteView.as_view(), name='artista-delete'),
			]