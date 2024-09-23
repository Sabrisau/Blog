from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

# Vista para listar todas las publicaciones
class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'  # Plantilla que mostrará la lista
    context_object_name = 'posts'  # Nombre de la variable de contexto en la plantilla
    ordering = ['-published_at']  # Ordenar por fecha de publicación descendente

# Vista para ver el detalle de una publicación específica
class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'  # Plantilla para el detalle de la publicación
    context_object_name = 'post'  # Nombre de la variable de contexto en la plantilla

# Vista para crear una nueva publicación (solo usuarios autenticados)
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']  # Campos que se mostrarán en el formulario
    template_name = 'post/post_form.html'  # Plantilla para el formulario de creación
    success_url = reverse_lazy('post-list')  # Redirigir a la lista de publicaciones tras crear

    # Asigna el usuario autenticado como el autor del post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Vista para editar una publicación (solo para el autor de la publicación)
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']  # Campos editables
    template_name = 'post/post_form.html'  # Reutiliza la misma plantilla de creación
    success_url = reverse_lazy('post-list')  # Redirige a la lista de publicaciones tras editar

    # Verifica si el usuario autenticado es el autor de la publicación
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Vista para eliminar una publicación (solo para el autor de la publicación)
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'  # Plantilla para confirmar eliminación
    success_url = reverse_lazy('post-list')  # Redirige a la lista de publicaciones tras eliminar

    # Verifica si el usuario autenticado es el autor de la publicación
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
