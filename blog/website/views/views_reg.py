from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from website.models import Post
from website.forms import RegForm, LoginForm


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


def auth_login(request):
    form = LoginForm()
    if request.method == 'GET':
        return render(request, 'website/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            password = form.data['password']
            user = authenticate(email=email, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("/account")
            else:
                return render(request, 'website/login.html',{'form': form})
        else:
            return render(request, 'website/login.html',{'form': form})

def registration(request):
    form = RegForm()
    #form = PostForm()
    if request.method == 'GET':
        return render(request, 'website/reg.html', {'form': form})
    elif request.method == 'POST':
        form = RegForm(request.POST)
        #form = PostForm(request.POST)
        if form.is_valid():
            email = form.data['email']
            password = form.data['password1']
            user = User.objects.create_user(email, password)
            user = authenticate(email=email, password=password)
            login(request, user)
            return redirect("/account")
        return render(request, 'website/reg.html', {'form': form})
        #return redirect("/")
