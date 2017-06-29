from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["greeting"] = "Hello World"
        context["stripe_pk_key"] = settings.PINAX_STRIPE_PUBLIC_KEY;
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"
