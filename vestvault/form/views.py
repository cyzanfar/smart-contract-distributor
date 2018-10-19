from django.shortcuts import render
from .models import Token
from .forms import TokenForm, HolderFormSet
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = TokenForm()
    return render(request, 'token_form.html', { 'form': form })

def home(request):
    t = Token.objects.first()
    return render(request, "home.html", {})
