from django.shortcuts import render
from django.views.generic import ListView, CreateView
from tp_final.models import Post
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    return render(request, "tp_final/index.html", {})

class PostList(ListView):
    model = Post
    template_name = "tp_final/post_list"

class PostCrear(CreateView):
    model = Post
    success_url = reverse_lazy("tp_final-listar")
    fields = '__all__'
