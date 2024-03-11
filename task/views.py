from django.shortcuts import render, redirect
from .models import *
from .forms import Videoform

# Create your views here.


def video(request):
    return render(request, "flights/index.html", {
        "videos": Video.objects.all()
    })

def flights(request):
    if request.method == "post":
       airtpost = Airtport(code="code", city="city")
    return render(request, 'flights/flight.html', {
        "flights": Flight.objects.all()
    })

def upload(request):
    form = Videoform()
    if request.method == 'POST':
        form = Videoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flights')
    context = {'form': form}
    return render(request, 'flights/form.html', context)

def updateFlight(request, pk):
    video = Video.objects.get(id=pk)
    form = Videoform(instance=video)
    if request.method  == "POST":
        form = Videoform(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('fligths')
    return render(request, 'flights/form.html', {
        'form': form
    })

def deleteFligth(request, pk):
    flight = Flight.objects.get(id=pk)
    if request.method == 'POST':
        flight.delete()
        return redirect('fligths')


        


