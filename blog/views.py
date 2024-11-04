from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def about(request):
    return render(request, 'blog/about.html')

def base(request):
    return render(request, 'base.html')

def navbar(request):
    return render(request, 'blog/navbar.html')