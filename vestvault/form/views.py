from django.shortcuts import render
from .models import Token
# Create your views here.

from django.http import HttpResponse


def index(request):
    t = Token.objects.first()
    #return HttpResponse("Hey {}, your token is {}.".format(t.company_name, t.token_name))
    return render(request, 'form/home.html', {'t':t})
    #return render(request, 'home.html')
def general(request):
    return render(request, 'home.html', {})

def home(request):
    return render(request, "home.html", {})