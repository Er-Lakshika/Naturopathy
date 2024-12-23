from django.shortcuts import path
from . import views

urlpatterns = [
    path(" ", views.index, name="index.html"),
    path("profile.html", views.profile, name= "profile.html"),
    path("introduction.html", views.introduction, name= "introduction.html"),
    path("form.html", views.form, name= "form.html"),
    path("naturopath.html", views.naturopath, name= "naturopath.html")
]