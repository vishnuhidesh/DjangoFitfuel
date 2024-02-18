from django.shortcuts import render

# Create your views here.

def mediterraneanDiet(request):
    return render(request,'Mediterranean.html')