from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Komentarz
from .forms import PostForm, KomentarzForm
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group



#def home(request):
#    return render(request, 'index.html', {})

class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class Postview(DetailView):
    model = Post
    template_name = 'post_widok.html'

class DodajPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'dodaj_post.html'
    # fields = '__all__'

class EdytujPostView(UpdateView):
    model = Post
    template_name = 'edycja_postu.html'
    fields = ['tytul', 'tresc']

class UsunPostView(DeleteView):
    model = Post
    template_name = 'usun_post.html'
    success_url = reverse_lazy('index')

class DodajKomnetarzView(CreateView):
    model = Komentarz
    form_class = KomentarzForm
    template_name = 'dodaj_komentarz.html'
    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('index')
