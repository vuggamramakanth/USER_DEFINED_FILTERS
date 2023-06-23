from django.shortcuts import render

# Create your views here.

def filters(request):
    d={'data':'HAi How ARE yoU'}
    return render(request,'filters.html',d)