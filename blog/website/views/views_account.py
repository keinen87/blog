from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as logout_action
from django.contrib.auth.decorators import login_required
from website.forms import UserForm


# LOGIN_URL = '/login'
@login_required(login_url='/')
def account(request):
    #import ipdb; ipdb.set_trace()
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        #import ipdb; ipdb.set_trace()
        if form.is_valid():
            form.save()
    return render(request, "website/account.html",{
    'user': request.user,
    'form': form
    })



def logout(request):
    logout_action(request)
    return redirect("/")
