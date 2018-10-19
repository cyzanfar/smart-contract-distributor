from django.shortcuts import render
from .models import Token
from .forms import TokenForm
from django.http import HttpResponse


# def index(request):
#     t = Token.objects.first()
#     return HttpResponse("Hey {}, your token is {}.".format(t.company_name, t.token_name))

def index(request):
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = TokenForm()
    return TokenForm(request, 'home.html', {'form': form})
