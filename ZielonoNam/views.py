from django.views.generic import TemplateView
from .settings import DEBUG


class IndexView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'