from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


posts = [
    {
        'author': 'aruni',
        'title':'Django tutorial',
        'content':'First turorial',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'mishra',
        'title':'Django web app',
        'content':'Second turorial',
        'date_posted': 'August 27, 2021'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }

    # return HttpResponse('hello world')
    return render(request, 'blog/home.html', context)

def about(request):

    return render(request, 'blog/about.html', {'title':'About page'})