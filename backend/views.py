from django.shortcuts import render
from .models import *

def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'index.html', context)


def article(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post': post
    }
    return render(request, 'article.html', context) 

def contact(request):
    return render(request, 'contact.html')  

def about(request):
    return render(request, 'about.html')      

def travel(request):
    return render(request, 'travel.html')         