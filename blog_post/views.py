from django.shortcuts import render

# Create your views here.
def blogview(request):
    return render(request,'blog.html')

def detailview(request):
    return render(request,'gallery-single.html')
