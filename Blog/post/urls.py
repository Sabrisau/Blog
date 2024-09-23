from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post-list'),  # Lista de publicaciones
    path('create/', views.PostCreateView.as_view(), name='post-create'),  # Crear publicación
    path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),  # Detalle de publicación
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post-edit'),  # Editar publicación
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),  # Eliminar publicación
]
