from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world! Awesome money managing app coming soon! :)")