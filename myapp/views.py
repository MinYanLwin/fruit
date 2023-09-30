from django.shortcuts import render,get_object_or_404
from .models import Fruit
# Create your views here.
def index(request):
    fruits=Fruit.objects.all()
    return render(request,'myapp/index.html',{'fruits':fruits})

def detail(request,slug):
    fruit=get_object_or_404(Fruit,slug=slug)
    return render(request,'myapp/detail.html',{
        'name':fruit.name,
        'price':fruit.price,
        'is_avaliable':fruit.is_avaliable
    })

