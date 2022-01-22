from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'})

def about(request):
    return render(request, 'rango/index.html', context=context_dict)

