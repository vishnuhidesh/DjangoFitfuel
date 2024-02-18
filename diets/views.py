from django.shortcuts import render

# Create your views here.
def recommendFunction(request):
    return render(request,'recommend.html') 

def medDiet(request):
    return render(request,'Med.html')
def ketoDiet(request):
    return render(request,'Keto.html')
def paleoDiet(request):
    return render(request,'Paleo.html')
def dashDiet(request):
    return render(request,'Dash.html')
def zoneDiet(request):
    return render(request,'Zone.html')
def balDiet(request):
    return render(request,'Bal.html')
def interDiet(request):
    return render(request,'Inter.html')