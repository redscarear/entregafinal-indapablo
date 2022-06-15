from django.urls import path
from evento import views
app_name='evento'
urlpatterns = [
    		path('evento', views.EventoListView.as_view(), name='evento-list'),
    		path('evento/add/', views.EventoCreateView.as_view(), name='evento-add'),
    		path('evento/<int:pk>/detail', views.EventoDetailView.as_view(), name='evento-detail'),
    		path('evento/<int:pk>/update', views.EventoUpdateView.as_view(), name='evento-update'),
    		path('evento/<int:pk>/delete', views.EventoDeleteView.as_view(), name='evento-delete'),
]