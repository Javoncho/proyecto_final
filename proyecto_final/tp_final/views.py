from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, "tp_final/index.html", {})

class PostList(TemplateView):
    template_name = "tp_final/post_list"
