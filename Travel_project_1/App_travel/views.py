from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import People

# Create your views here.


def fun1(request):
    obj=Place.objects.all() #this means to assingn all the contents in the table Place on to obj
    ppl=People.objects.all()
    return render(request,"index.html", {'result':obj, "result2":ppl})

#orm (object relation map)

