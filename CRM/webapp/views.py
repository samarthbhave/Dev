from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return HttpResponse("Hello Omkar")
    return render(request, 'webapp/index.html')
