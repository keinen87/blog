from django.shortcuts import render, get_object_or_404, redirect
from website.models import Post
from django.core.paginator import Paginator, EmptyPage
from django import forms
from django.contrib.auth import get_user_model

def home(request):
    # POST http://example.com/?name=alex&age=21&go=total request.POST
    #import ipdb; ipdb.set_trace()
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = 1
    if 'page' in request.GET:
        page = int(request.GET['page'])
    try:
        posts = paginator.page(page)
    except EmptyPage:
       posts = paginator.page(paginator.num_pages)
    return render(request, 'website/index.html',{'posts':posts})

def post_view(request, slug):
    # select name, surname from users;
    # select name, surname from users limit 10 offset 0;
    # select name, surname from users limit 10 offset 10; 20 30 40 50
    # offset 10 * (page - 1)
    # URL http://ya.ru/?df=12&name=test&p=0
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'website/post.html', {'post':post})
