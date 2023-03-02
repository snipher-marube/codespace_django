from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'core/index.html',context)


def home(request):
    context = {}
    return render(request, 'core/home.html',context)