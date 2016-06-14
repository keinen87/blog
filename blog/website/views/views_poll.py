from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from website.forms import Poll1, Poll2, Poll3

# /pool/?step=3
def poll(request):
    step = 1
    if 'step' in request.GET:
        step = int(request.GET['step'])
    pools = {
        1: Poll1,
        2: Poll2,
        3: Poll3
    }
    form = pools[step]()
    if request.method == 'GET':
        return render(request, 'website/poll.html', {'form': form})
    elif request.method == 'POST':
        form = pools[step](request.POST)
        if form.is_valid():
            # state save
            # FIXME:
            if step == 3:
                return redirect('/')
            else:
                return redirect('/poll/?step=' + str(step + 1))
        else:
            return render(request, 'website/poll.html', {'form': form})
