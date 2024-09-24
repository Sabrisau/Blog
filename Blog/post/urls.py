from django.urls import path
from .views import home_view, ListaPublicacionesView, CrearPublicacionView, RegistroUsuario, DetallePublicacionView, ActualizarPublicacionView, EliminarPublicacionView

urlpatterns = [
    path('', home_view, name='home'),
    path('publicaciones/', ListaPublicacionesView.as_view(), name='lista_publicaciones'),
    path('/posts/create/', CrearPublicacionView.as_view(), name='crear_publicacion'), 
    path('/posts/<int:pk>/', DetallePublicacionView.as_view(), name='detalle_publicacion'), 
    path('/posts/<int:pk>/edit/', ActualizarPublicacionView.as_view(), name='editar_publicacion'),  
    path('/posts/<int:pk>/delete/', EliminarPublicacionView.as_view(), name='eliminar_publicacion'), 
]
