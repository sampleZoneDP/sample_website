from django.shortcuts import render, render_to_response, RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import LoginForm
# Create your views here.
def home(request):
    return render_to_response("signup.html",
                              locals(),
                              context_instance=RequestContext(request))

def single(request):
    return render_to_response("single.html",
                              locals(),
                              context_instance=RequestContext(request))
def login(request):    
    return render_to_response("login.html",
                              locals(),
                              context_instance=RequestContext(request))

def checkout(request):
    return render_to_response("checkout.html",
                              locals(),
                              context_instance=RequestContext(request))

def register(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('/registered/')
    return render_to_response("register.html",
                              locals(),
                              context_instance=RequestContext(request))

def shop(request):
    return render_to_response("shop.html",
                              locals(),
                              context_instance=RequestContext(request))

def registered(request):
    return render_to_response("registered.html",
                              locals(),
                              context_instance=RequestContext(request))
    



