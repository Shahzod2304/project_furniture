from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

def Blog(request):
    return render(request, 'blog.html')

def Contact(request):
    return render(request, 'contact.html')

def Furniture(request):
    return render(request, 'furniture.html')