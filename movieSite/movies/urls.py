from django.urls import path

from . import views

urlpatterns = [
    path("", views.MoviesView.as_view()),
    path(r"<int:pk>/", views.MovieDetailView.as_view()),
]
