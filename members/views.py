# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

def index(request):
    context = {
        'mymembers': Members.objects.all().values()
    }
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def test(request):    
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def add(request):    
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def add(request):    
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addrecord(request):
    x = request.POST['firstname']
    y = request.POST['lastname']
    member = Members(firstname = x, lastname = y)
    member.save()
    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    member = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': member,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, id):
    member = Members.objects.get(id=id)
    x = request.POST['firstname']
    y = request.POST['lastname']
    member = Members.objects.get(id=id)
    member.firstname = x
    member.lastname = y
    member.save()
    return HttpResponseRedirect(reverse('index'))
