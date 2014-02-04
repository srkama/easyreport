# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.http import *
from django.template import RequestContext

@login_required(login_url='/login/')
def add_user(request):
    return render_to_response("add_user.html")


def user_login(request):
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            return HttpResponseRedirect('/adduser/')
    return render_to_response("login.html", context_instance = RequestContext(request))