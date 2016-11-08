from django import forms
from website.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','short_desc','description']

class PostCommentForm(forms.Form):
    post_text = forms.CharField(widget=forms.Textarea, label="Комментарий")
