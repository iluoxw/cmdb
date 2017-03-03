# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,JsonResponse
from models import User
import time


def r404(request):
    return render_to_response("userTemplate/404.html", locals())


def login(request):
    if request.method == "POST" and request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
            if user.password == password:
                response =  HttpResponseRedirect("/index")
                response.set_cookie("username",username,3600)
                request.session["username"] = username+time.strftime("%H:%M:%S")
                return response

            else:
                return HttpResponseRedirect("/User/login")
        except:
            return HttpResponseRedirect("/User/login")

    else:
        # return HttpResponseRedirect("r404")
        return render_to_response("userTemplate/login.html")



def register(request):
    return render_to_response("userTemplate/register.html",locals())


def userValid(request):
    if request.method == "POST" and request.POST:
        status = {"valid":"successs"}
        try:
            print (request.POST)
            print (dir(request.POST))
            username = request.POST.get("user")
            object = User.objects.filter(username=username)
            if object:
                status["valid"] = "error"
        except Exception as e:
            print e
        return JsonResponse(status)
    else:
        return render_to_response("userTemplate/register.html",locals())
# Create your views here.
