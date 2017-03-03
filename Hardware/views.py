from django.shortcuts import render_to_response
from models import *

def index(request):
    return render_to_response("hardwareTemplate/index.html", locals())


def hardwarelist(request):
    hardwareData = Hardware.objects.all()
    return render_to_response("hardwareTemplate/hardwarelist.html", locals())


