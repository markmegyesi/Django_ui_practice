from django.shortcuts import render
from .models import PostsModel
# Create your views here.



def home(request):
    posts = PostsModel.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')