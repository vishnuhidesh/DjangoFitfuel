from django.shortcuts import render

def landingFunction(request):
    return render(request,'landing.html')

def navbarFunction(request):
    return render(request,'navbar.html')

def chartsFunction(request):
    return render(request,'charts.html')