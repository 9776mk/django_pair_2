from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def main(request):
    return render(request, "movies/main.html")

def index(request):
    movies = Movie.objects.all()
    context = {
        "movies": movies
    }

    return render(request, "movies/index.html", context)