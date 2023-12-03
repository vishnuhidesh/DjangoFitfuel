from django.shortcuts import render

# Create your views here.

def editProfileFunction(request):
    return render(request,"editprofile.html")