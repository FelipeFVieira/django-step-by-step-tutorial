from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello Developer, this is your first view!")