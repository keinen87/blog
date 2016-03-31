from django.shortcuts import render

# Create your views here.

def home(request):
    demo_model = {
      'title': "Какой то загловок",
      'pub_date': "01.01.2016",
      'user': "Вася",
      'description': "<h3>Привет!</h3>"
    }
    posts = [demo_model,demo_model,demo_model]
    return render(request, 'website/index.html',{'posts':posts})
