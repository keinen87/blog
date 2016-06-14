from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from website.forms import Poll1, Poll2, Poll3

def poll1(request):
    form1 = Poll1()
    if request.method == 'GET':
        return render(request, 'website/poll.html', {'form': form1})
    elif request.method == 'POST':
        form1 = Poll1(request.POST)
        if form1.is_valid():
            return redirect("/poll2")

def poll2(request):
    form2 = Poll2()
    if request.method == 'GET':
        return render(request, 'website/poll.html', {'form': form2})
    elif request.method == 'POST':
        form2 = Poll2(request.POST)
        if form2.is_valid():
            return redirect("/poll3")

def poll3(request):
    form3 = Poll3()
    if request.method == 'GET':
        return render(request, 'website/poll.html', {'form': form3})
    elif request.method == 'POST':
        form3 = Poll3(request.POST)
        if form3.is_valid():
            return redirect("/")
