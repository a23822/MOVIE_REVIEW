from django.urls import path
from . import views

app_name = 'movies'
urlpatterns = [
    path('', views.list, name='list'),
    path('<int:movie_id>/detail/', views.detail, name="detail"),
    path('<int:movie_id>/<int:score_id>/delete', views.score_delete, name="score_delete"),
]
