from django.http import HttpResponse
import datetime

def index(request):
    datetime.datetime.now()

    return HttpResponse("Hello, world. You're at the polls index.")