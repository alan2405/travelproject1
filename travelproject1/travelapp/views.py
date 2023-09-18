from django.shortcuts import render
from django.shortcuts import HttpResponse
from . models import Place,Team
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 =Team.objects.all()
    #return render(request,"index.html",{'result':obj})
    return render(request,"index.html",{'result1':obj1,'result':obj})
