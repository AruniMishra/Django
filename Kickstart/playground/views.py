from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x=1
    y=2
    return x + y

# Create your views here.

def say_hello(request):
    #return HttpResponse('hello world')
    a = 1
    b = 2
    a = calculate()
    return render(request, 'hello.html', {'name':'aruni'})