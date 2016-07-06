from django.views.generic import ListView, DetailView
from website.models import Post, CustomUser

class PostListView(ListView):
    model = Post
    template_name = 'website/index.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    template_name = 'website/index.html'
    context_object_name = 'post'
    #query_pk_and_slug = True
    #pk_url_kwarg = 'slug'
    slug_field = 'slug'
