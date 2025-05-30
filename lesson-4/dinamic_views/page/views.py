from django.shortcuts import render

def home(request):
    context = {
        'name': 'Felipe',
        'job': 'CyberSec'
    }

    return render(request, 'page/home.html', context)

