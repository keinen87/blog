from django.views.generic import ListView
from website.models import Post, CustomUser

class PostListView(ListView):
    model = Post
    template_name = 'website/index.html'
    context_object_name = 'posts'
    paginate_by = 2
