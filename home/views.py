from django.shortcuts import render
from home.models import Home


def home_index(request):
    home_query = Home.objects.all()
    context = {"home_query": home_query}
    return render(request, "home_index.html", context)
