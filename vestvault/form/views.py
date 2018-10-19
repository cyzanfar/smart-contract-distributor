from django.shortcuts import render
from .models import Token
from .forms import TokenForm, HolderForm
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        import pdb; pdb.set_trace()
        form = TokenForm(request.POST)
        if form.is_valid():
            pass
    else:
        holder_form = HolderForm()
        form = TokenForm()
    return render(request, 'token_form.html', {'form': form, 'holder_form': holder_form})

def home(request):
    t = Token.objects.first()
    return render(request, "home.html", {})
