from django.shortcuts import render

# Create your views here.

def blog(request):
    if request.method=='GET':
        return render(request,'blog/blog.html',{})