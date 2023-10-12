from django.shortcuts import render, redirect
from .models import Iphone

# Create your views here.
def home(request):
    iphone = Iphone.objects.all()
    context = {'iphone_list':iphone

    }
    return render(request,'home.html',context)

def details(request,id):
    iphone = Iphone.objects.get(id=id)
    return render(request,'details.html',{'iphone':iphone})

def add_iphone(request):
        if request.method == 'POST':
          name = request.POST.get('name')
          desc = request.POST.get('desc')
          price = request.POST.get('price')
          img = request.FILES['img']
          iphone = Iphone(name=name,desc=desc,price=price,img=img)
          iphone.save( )
          return redirect('/')
        return render(request,'add.html')

def cart(request,id):
    if request.method == 'POST':
        iphone = Iphone.objects.get(id=id)
        iphone.delete()
        return redirect('/')
    return render(request,'cart.html')
