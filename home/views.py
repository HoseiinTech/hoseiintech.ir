from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.views.generic import DetailView, FormView

from home.models import AboutMe, Resume
from home.forms import ContactForm


class AboutMeView(DetailView):
    context_object_name = 'about_me'
    template_name = 'home/index.html'

    def get_object(self, queryset=None):
        instance = AboutMe.objects.filter(status=True).first()
        return instance


class MyResumeView(DetailView):
    context_object_name = 'my_resume'
    template_name = 'home/resume.html'

    def get_object(self, queryset=None):
        instance = Resume.objects.filter(status=True).first()
        return instance


class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("home:about")

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        from_email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        send_mail(
            f"New contact form submission from {name}",
            message,
            from_email,
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False
        )
        return super().form_valid(form)
