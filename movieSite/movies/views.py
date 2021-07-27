from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie


class MoviesView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "поле для недефолтных имен шаблона"


class MovieDetailView(DetailView):
    """Полное описание фильма"""
    model = Movie
    slug_field = "url"

    # code review class(View)
    # def get(self, request, slug):
    #     movie = Movie.objects.get(url=slug)
    #     return render(request, "movies/movie_detail.html", {"movie": movie})


# class AddReview(View):
#     """Отзывы"""
#     def post(self, request, pk):
#         print(request.POST)
#         return redirect("/")
