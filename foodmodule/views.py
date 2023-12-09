from django.shortcuts import render

# Create your views here.

def scanFunction(request):
    return render(request, 'imagetake.html')


def analyse(request):
    pass