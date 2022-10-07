from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def main(request):
    return render(request, "movies/main.html")


def index(request):
    movies = Movie.objects.all()
    context = {"movies": movies}

    return render(request, "movies/index.html", context)


def detail(request, pk):
    movie = Movie.objects.get(pk=pk)

    context = {"movie": movie}

    return render(request, "movies/detail.html", context)


def delete(request, pk):
    Movie.objects.get(pk=pk).delete()
    return redirect("movies:index")
