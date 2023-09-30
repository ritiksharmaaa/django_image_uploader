from django.shortcuts import render
from .models import image 
from .forms import imageForm
from django.contrib import messages 
from django.http import HttpResponseRedirect
# Create your views here.
print(messages)

def home(request):
    if request.method == "POST":
        form = imageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request , "Image Uploaded Successfully  !!" )
            return HttpResponseRedirect("/")

    else:
        form = imageForm()
    im = image.objects.all().order_by("-id")
    context={'form' : form , 'images' : im }
   
    return render(request , 'myapp/home.html' , context  )

