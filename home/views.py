from django.shortcuts import render
from home.models import Home
from django.views.generic import TemplateView


def home_index(request):
    home_query = Home.objects.all()
    context = {"home_query": home_query}
    return render(request, "home_index.html", context)


class AboutView(TemplateView):
    template_name = "about.html"
