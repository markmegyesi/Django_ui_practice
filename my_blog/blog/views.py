from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {'author': 'Megyesi Márk',
     'title': 'Blog post 1',
     'content': 'First content',
     'date_posted': '2022.szeptember.14'},
     {'author': 'Megyesi Márk',
     'title': 'Blog post 2',
     'content': 'second content',
     'date_posted': '2022.szeptember.12'},
     {'author': 'Megyesi Márk',
     'title': 'third content',
     'date_posted': '2022.szeptember.11'},
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context=context)

def about(request):
    return render(request, 'blog/about.html')