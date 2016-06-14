from django import forms

class Poll1(forms.Form):
    name = forms.CharField(required=True,widget=forms.Textarea,min_length=2,max_length=20)
    age = forms.IntegerField(required=True,widget=forms.NumberInput,min_value=5,max_value=100)
    def clean(self):
        cleaned_data = super().clean()
        age = cleaned_data.get("age")
        if age < 0:
            self.add_error("age","Invalid age!")

class Poll2(forms.Form):
    que1 = forms.CharField(required=True)
    que2 = forms.CharField(required=True)
    que3 = forms.CharField(required=True)

class Poll3(forms.Form):
    comment = forms.CharField(required=True)
