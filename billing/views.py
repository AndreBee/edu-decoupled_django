from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# login is required to access this view
class Index(LoginRequiredMixin, TemplateView):
    template_name = "billing/index.html"
