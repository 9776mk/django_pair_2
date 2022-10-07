from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.


def main(request):
    return render(request, "movies/main.html")
