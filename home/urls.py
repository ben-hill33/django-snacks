from django.urls import path
from . import views
from .views import AboutView

urlpatterns = [
    path("", views.home_index, name="home_index"),
    path("about", AboutView.as_view(), name="about"),
]
