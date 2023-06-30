from django.shortcuts import render
from django.views.generic import DetailView

from home.models import AboutMe


class AboutMeView(DetailView):
    context_object_name = 'about_me'
    template_name = 'home/index.html'

    def get_object(self, queryset=None):
        instance = AboutMe.objects.filter(status=True).first()
        return instance


def resume(request):
    return render(request, 'home/resume.html')


def contact(request):
    return render(request, 'home/contact.html')
