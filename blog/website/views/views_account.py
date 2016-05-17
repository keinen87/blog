from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as logout_action
from django.contrib.auth.decorators import login_required


# LOGIN_URL = '/login'
@login_required(login_url='/')
def account(request):
    return render(request, "website/account.html",{'user': request.user})

def logout(request):
    logout_action(request)
    return redirect("/")
