from django.urls import path
from tecnico import views
app_name='tecnico'
urlpatterns = [
    			path('tecnico', views.TecnicoListView.as_view(), name='tecnico-list'),
    			path('tecnico/add/', views.TecnicoCreateView.as_view(), name='tecnico-add'),
    			path('tecnico/<int:pk>/detail', views.TecnicoDetailView.as_view(), name='tecnico-detail'),
    			path('tecnico/<int:pk>/update', views.TecnicoUpdateView.as_view(), name='tecnico-update'),
    			path('tecnico/<int:pk>/delete', views.TecnicoDeleteView.as_view(), name='tecnico-delete'),
			]