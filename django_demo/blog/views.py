from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'SerhiiY',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'June 23 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 23 2019'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
