from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login_page')
def success(request):
   
    if (request.method == 'POST'):
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image=request.FILES.get('recipe_image')

        Recipe.objects.create(
             recipe_name =  recipe_name ,
             recipe_description=recipe_description,
             recipe_image = recipe_image

        )
        return redirect('/home/')
    data=Recipe.objects.all()
    if request.GET.get('search'):
         data=data.filter(recipe_name__icontains=request.GET.get('search'))
    context={'data':data}
    return render(request,'home/home.html',context)


def delete(request,pk):
        data=Recipe.objects.get(id=pk)
        if (data):
           data.delete()
           return redirect('/home/')
        return render(request,'home/home.html')

def update(request,pk):
        data=Recipe.objects.get(id=pk)
        context={'data':data}
        if request.method=="POST":
             recipe_name=request.POST.get('recipe_name')
             recipe_description=request.POST.get('recipe_description')
             recipe_image=request.FILES.get('recipe_image')

             data.recipe_name=recipe_name
             data.recipe_description=recipe_description
             if recipe_image:
               data.recipe_image=recipe_image
             data.save()
             return redirect('home')

        return render(request,'home/update.html',context)
        
             
def login_page(request):
        if request.method=="POST":
          username=request.POST.get('username')
          password = request.POST.get('password')
          
          if not User.objects.filter(username=username).exists():
                messages.error(request, "invalid username.")
                return redirect('login_page')
          user = authenticate(username=username, password=password)
          if user is None:
               messages.error(request, "Invalid password")
               return redirect('login_page')
          else:
               messages.success(request, "success password")
               login(request,user)
               return redirect('home')
        return render(request,'home/login.html')
        
               
                   
       
def logout_page(request):
     logout(request)
     return redirect('login_page')



def register(request):
     
     if request.method=="POST":
          username=request.POST.get('username')
          password = request.POST.get('password')

          user=User.objects.filter(username=username)
          if user.exists():
               messages.error(request, " User already exists.")
               return redirect('register')
          

          user =User.objects.create(
               username=username,
          )
          user.set_password(password)
          user.save()
          messages.success(request, " registered successfully.")
          return redirect('register')
         


     return render(request,'home/register.html')           
       
        


       


   
