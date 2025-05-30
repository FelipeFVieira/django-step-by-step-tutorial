from django.shortcuts import render

def home(request):
    context = {
        'name': 'your-name',
        'job': 'your-job'
    }

    return render(request, 'page/home.html', context)

