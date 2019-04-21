from django.shortcuts import render,redirect, get_object_or_404
from .models import Movie, Genre, Score
from .forms import ScoreForm

# Create your views here.
def list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/list.html', {
        'movies':movies,
    })

def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == "GET":
        score = Score.objects.filter(movie_id=movie_id)
        form = ScoreForm
        return render(request, 'movies/detail.html', {
            'movie':movie,
            'scores':score,
            'form':form,
        })
    else:
        form = ScoreForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user_id = request.user
            comment.movie_id = movie
            comment.save()
        else:
            return redirect('movies:list')
        return redirect('movies:detail', movie_id)
        
def score_delete(request, movie_id, score_id):
    score = get_object_or_404(Score, pk=score_id)
    
    score.delete()
    
    return redirect('movies:detail', movie_id)