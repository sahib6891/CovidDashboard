from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    context = {'a': 'a'}
    return render(request, 'index.html', context=context)