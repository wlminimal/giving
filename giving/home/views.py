from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["greeting"] = "Hello World"
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"

