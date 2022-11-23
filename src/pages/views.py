from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *arg, **kwargs):
    return render(request, "home.html", {})

def contact_view(request, *arg, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *arg, **kwargs):
    my_context = {
        "my_text": "This is about me",
        "my_number": 123,
        "my_list": [123, 456, 789]
    }
    return render(request, "about.html", my_context)

def social_view(request, *arg, **kwargs):
    return render(request, "social.html", {})