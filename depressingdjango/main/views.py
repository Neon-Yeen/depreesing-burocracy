from math import prod
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from  .forms import clienteform, tecnicoform, abogadoform
from .models import product

def index(response):
     return render(response, "main/index.html",{})

def e404(response):
     return render(response, "main/404.html",{})


def aboutus(response):
     return render(response, "main/aboutus.html",{})


def login(response):
     return render(response, "main/login.html",{})

     
def signin(response):
     return render(response, "main/signin.html",{})

def termsservices(response):
     return render(response, "main/termsservices.html",{})


def create(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form1 = clienteform(request.POST or None)
    form2 = tecnicoform(request.POST or None)
    form3 = abogadoform(request.POST or None)

    if form1.is_valid():
        form1.save()
        return HttpResponseRedirect("/list")
    if form2.is_valid():
        form2.save()
        return HttpResponseRedirect("/list")
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect("/list")

    context['form1']= form1
    context['form2']= form2
    context['form3']= form3
    return render(request, "main/create.html", context)

def list(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = product.objects.all()
         
    return render(request, "main/list.html", context)

def view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["data"] = product.objects.get(id = id)
         
    return render(request, "main/view.html", context)

def update(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(product, id = id)
 
    # pass the object as instance in form
    form1 = clienteform(request.POST or None, instance = obj)
    form2 = tecnicoform(request.POST or None,instance = obj)
    form3 = abogadoform(request.POST or None,instance = obj)

    if form1.is_valid():
        form1.save()
        return HttpResponseRedirect("/list")
    if form2.is_valid():
        form2.save()
        return HttpResponseRedirect("/list")
    if form3.is_valid():
        form3.save()
        return HttpResponseRedirect("/list")

    context['form1']= form1
    context['form2']= form2
    context['form3']= form3
 
    return render(request, "main/update.html", context)

def delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(product, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/list")
 
    return render(request, "main/delete.html", context)
