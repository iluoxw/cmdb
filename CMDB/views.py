from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from User.models import *


def index(request):
    try:
        u = request.COOKIES["username"] and request.session["username"]
        p = username = request.COOKIES["username"]
        return render_to_response("index.html",locals())
    except:
        return HttpResponseRedirect("/User/login")
    # return render_to_response("index.html", locals())


def cookietest(request):
    cookies = request.COOKIES

    response = render_to_response("cookietest.html", locals())
    response.set_cookie("data", {"name": "luoxw", "age": 18}, 3600)
    return response


def session(request):
    request.session["name"] = "luoxiaowei"
    request.session["age"] = 28

    validsession = request.session["name"]
    return render_to_response("session.html", locals())


def logout(request):
    try:
        del request.COOKIES["username"]
        del request.session["username"]
    except:
        pass
    return HttpResponseRedirect("/User/login",locals())