from django.shortcuts import render, get_object_or_404, redirect
from website.models import Post
from django.core.paginator import Paginator, EmptyPage
from django import forms
from django.contrib.auth import get_user_model
from website.forms.form_post import PostCommentForm
from website.models import Comments

def home(request):
    # POST http://example.com/?name=alex&age=21&go=total request.POST
    # import ipdb; ipdb.set_trace()
    posts = Post.no_draft.all()
    if "sort" in request.GET:
        sort_by = request.GET["sort"]
        posts = posts.order_by(sort_by)
    paginator = Paginator(posts, 5)
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
    form = None
    post = get_object_or_404(Post, slug=slug)
    comments = Comments.objects.filter(post = post, pub_date__isnull=False)
    no_form = False
    if post.owner == request.user:
        no_form = True
    if request.method == "GET":
        form = PostCommentForm()
        # import ipdb; ipdb.set_trace()
    elif request.method == "POST":
        form = PostCommentForm(request.POST)
        if form.is_valid():
            comment = Comments()
            comment.text = form.data["post_text"]
            comment.owner = request.user
            comment.post = post
            comment.save()
            form = PostCommentForm()
    return render(request, 'website/post.html', {
    'post':post, 'form': form, 'comments': comments,'no_form':no_form})
