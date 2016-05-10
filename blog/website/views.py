from django.shortcuts import render, get_object_or_404
from website.models import Post
from website.pagination import Pagination

# Create your views here.

def home(request):
    pag = Pagination()
    posts = Post.objects.all()
    #import ipdb; ipdb.set_trace()
    if 'page' in request.GET:
        page = int(request.GET['page'])
        posts = pag.get_data(posts, page)    
    """    demo_model = {
      'title': "Какой то загловок",
      'pub_date': "01.01.2016",
      'user': "Вася",
      'description': "<h3>Привет!</h3>"
    }
    posts = [demo_model,demo_model,demo_model]
    """
    return render(request, 'website/index.html',{'posts':posts})

def post_view(request, slug):
    # select name, surname from users;
    # select name, surname from users limit 10 offset 0;
    # select name, surname from users limit 10 offset 10; 20 30 40 50
    # offset 10 * (page - 1)
    # URL http://ya.ru/?df=12&name=test&p=0
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'website/post.html', {'post':post})
