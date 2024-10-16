from django.shortcuts import render
from django.http import JsonResponse 

# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request,"core/home.html")