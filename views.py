from django.shortcuts import render, redirect
from django.http import HttpResponse
from dataapp.forms import dataappForm
from django.contrib import messages
from django.urls import reverse
from .models import Person
# Create your views here.
def index(request):
    return render(request,'index.html')

#def person(request):
    if request.method == 'POST':
        form = dataappForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = dataappForm()
    return render(request,'person.html',{'form':form})

def person(request):
    all_person = Person.objects.all()
    return render(request, 'person.html',{'all_person' : all_person})

def form_view(request):
    if request.method=="POST":
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        gender = request.POST["gender"]
        address = request.POST["address"]
        new_person = Person(fname=fname,lname=lname,gender=gender,address=address)
        new_person.save()
        messages.success(request, 'บันทึกข้อมูลเรียบร้อย')
        return redirect(reverse('person'))
    else:
        return render(request, 'form_view.html', {})
    
def delete(request, person_id):
    delete_person = Person.objects.get(id=person_id)
    delete_person.delete()
    messages.error(request, "ลบข้อมูลเรียบร้อย")
    return redirect(reverse('person'))

def edit(request, person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.fname = request.POST["fname"]
        person.lname = request.POST["lname"]
        person.gender = request.POST["gender"]
        person.address = request.POST["address"]
        person.save()
        messages.success(request, "แก้ไขข้อมูลเรียบร้อย")
        return redirect(reverse('person'))
    else:
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person":person})