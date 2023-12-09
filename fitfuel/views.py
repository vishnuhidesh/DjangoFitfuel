from django.shortcuts import render

def landingFunction(request):
    return render(request,'landing.html')