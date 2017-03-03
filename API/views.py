from django.shortcuts import render_to_response
from django.http import JsonResponse


def index(request):
    return render_to_response("apiTemplate/index.html", locals())


def recvdata(request):
    result = {"status": ""}
    if request.method == "POST" and request.POST:
        result["status"] = "post"
    else:
        result["status"] = "get"
    return JsonResponse(result)

# Create your views here.
