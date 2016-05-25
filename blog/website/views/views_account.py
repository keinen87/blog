from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout as logout_action
from django.contrib.auth.decorators import login_required
from website.forms import UserForm
from website.models import Post
from website.forms import PostForm

@login_required(login_url='/')
def account(request):
    posts = Post.objects.filter(owner=request.user)
    return render(request, "website/account.html",{'posts':posts})

# LOGIN_URL = '/login'
@login_required(login_url='/')
def account_edit(request):
    #import ipdb; ipdb.set_trace()
    form = UserForm(instance=request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        #import ipdb; ipdb.set_trace()
        if form.is_valid():
            form.save()
    return render(request, "website/account_edit.html",{
    'user': request.user,
    'form': form
    })

@login_required(login_url='/')
def post_edit(request, slug):
    post = get_object_or_404(Post,slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
    return render(request,"website/post_edit.html",{'form':form})  

def logout(request):
    logout_action(request)
    return redirect("/")
