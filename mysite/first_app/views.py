from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    my_dict = {'insert_me' : "hello ive changed .py!"}
    return render(request,'mysite/index.html',context = my_dict)
      