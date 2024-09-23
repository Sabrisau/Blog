from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='lista publicaciones'), 
    path('crear/', views.PostCreateView.as_view(), name='crear publicacion'), 
    path('<int:pk>/', views.PostDetailView.as_view(), name='detalle publicacion'), 
    path('<int:pk>/editar/', views.PostUpdateView.as_view(), name='editar publicacion'),  
    path('<int:pk>/eliminar/', views.PostDeleteView.as_view(), name='eliminar publicacion'), 
]
