from django.shortcuts import render, get_object_or_404
from website.models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all()    
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
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'website/post.html', {'post':post})
