from django.urls import reverse_lazy
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


class ContactFormView(FormView):
    template_name = "home/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy('home:contact')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        form.send_email()
        return super().form_valid(form)
