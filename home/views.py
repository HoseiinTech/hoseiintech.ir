from django.shortcuts import render


def home(request):
    return render(request, 'home/index.html')


def resume(request):
    return render(request, 'home/resume.html')


def contact(request):
    return render(request, 'home/contact.html')
