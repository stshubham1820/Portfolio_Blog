from django.shortcuts import render
from .models import About
# Create your views here.


def home(request):
    return render(request,'index.html')

def about(request):
    #model_queries
    '''
    model.objects.create()
    model.objects.update()
    all
    get
    filter
    '''
    data = About.objects.filter(email='st18@mail.com')
    print(data)
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')