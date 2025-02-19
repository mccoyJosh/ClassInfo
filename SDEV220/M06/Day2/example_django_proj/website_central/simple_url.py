from django.http import HttpResponse


def simple_url(request):
    return HttpResponse("Here is the simple result")
