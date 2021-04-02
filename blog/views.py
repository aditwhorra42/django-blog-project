from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author": "Adit",
        "title": "First Blog",
        "content": "This is the first blog",
        "date_posted": "01/01/2021"
    },
    {
        "author": "Adit",
        "title": "Second Blog",
        "content": "This is the second blog",
        "date_posted": "01/03/2021"
    }
]

def home_view(request):
    context = {
        "posts": posts,
        "title": "Home"
    }
    return render(request, 'blog/home.html', context)

def about_view(request):
    return render(request, 'blog/about.html', {"title": "About"})