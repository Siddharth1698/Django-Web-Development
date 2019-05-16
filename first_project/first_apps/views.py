from django.shortcuts import render

# Create your views here.

def index(request):
    my_dict = {'insert_content':"Hello iam from first app!"}
    return render(request,'first_apps/index.html',context = my_dict)