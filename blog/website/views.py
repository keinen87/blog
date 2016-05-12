from django.shortcuts import render, get_object_or_404, redirect
from website.models import Post
from django.core.paginator import Paginator, EmptyPage
from django import forms

class RegForm(forms.Form):
    email = forms.CharField(required=True)
    password1 = forms.CharField(required=True,widget=forms.PasswordInput)
    password2 = forms.CharField(required=True,widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pas1 = cleaned_data.get("password1")
        pas2 = cleaned_data.get("password2")
        if pas1 != pas2:
            self.add_error("password1","Password mismatch!")

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

# Create your views here.

# post = yiled yield Post.objects.all()
# test(await post)
# print("OK")

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

def registration(request):
    regForm = RegForm()
    form = PostForm()
    if request.method == 'GET':
        return render(request, 'website/reg.html', {'form': form})
    elif request.method == 'POST':
        #regForm = RegForm(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'website/reg.html', {'form': form})
        #return redirect("/")
        
