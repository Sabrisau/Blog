from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class RegistroUsuario(CreateView):
    template_name = 'registro.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

class ListaPublicacionesView(ListView):
    model = Post
    template_name = 'lista.html'  
    ordering = ['-fecha']

    def get_queryset(self):
        queryset = super().get_queryset()
        autor_id = self.request.GET.get('autor')

        if autor_id:
            queryset = queryset.filter(autor_id=autor_id)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autores'] = User.objects.all()  # Obtener todos los usuarios
        return context

class DetallePublicacionView(DetailView):
    model = Post
    template_name = 'detalle.html'  

def home_view(request):
    view = ListaPublicacionesView.as_view()
    return view(request)

class CrearPublicacionView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['titulo', 'contenido']  
    template_name = 'formulario.html' 
    success_url = reverse_lazy('lista_publicaciones')  

    def form_valid(self, form):
        form.instance.autor = self.request.user  # Asigna el usuario autenticado como autor
        return super().form_valid(form)

class ActualizarPublicacionView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido']  
    template_name = 'formulario.html'  
    success_url = reverse_lazy('lista_publicaciones') 
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor  

class EliminarPublicacionView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'confirmacion_eliminacion.html'  
    success_url = reverse_lazy('lista_publicaciones') 

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_queryset(self):
        return Post.objects.filter(autor=self.request.user)
