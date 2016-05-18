from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

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
        if User.objects.filter(email=cleaned_data.get("email")).exists():
            self.add_error("email","Email exists")

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','avatar','phone','skype']
