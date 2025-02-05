from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def connect(request):
    return render(request, 'connect.html')

def learn(request):
    return render(request, 'learn.html')

def build(request):
    return render(request, 'build.html')

def use(request):
    return render(request, 'use.html')

def operate(request):
    return render(request, 'operate.html')

def news(request):
    return render(request, 'news.html')