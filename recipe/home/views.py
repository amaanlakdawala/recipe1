from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *

# Create your views here.

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
        
             
             
       
        


       


   
