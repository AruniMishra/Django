from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'aruni',
        'title':'Django tutorial',
        'content':'First turorial'
    },
    {
        'author': 'mishra',
        'title':'Django web app',
        'content':'Second turorial'
    }
]

def home(request):
    context = {
        'posts': posts
    }

    # return HttpResponse('hello world')
    return render(request, 'blog/home.html', context)

def about(request):

    return render(request, 'blog/about.html', {'title':'About page'})