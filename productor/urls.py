from django.urls import path
from productor import views
app_name='productor'
urlpatterns = [
    			path('productor', views.ProductorListView.as_view(), name='productor-list'),
    			path('productor/add/', views.ProductorCreateView.as_view(), name='productor-add'),
    			path('productor/<int:pk>/detail', views.ProductorDetailView.as_view(), name='productor-detail'),
    			path('productor/<int:pk>/update', views.ProductorUpdateView.as_view(), name='productor-update'),
    			path('productor/<int:pk>/delete', views.ProductorDeleteView.as_view(), name='productor-delete'),
			]