from django.db import models
from django.conf import settings
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Score(models.Model):
    content = models.CharField(max_length=40, blank=True)
    value = models.IntegerField()
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="comment_movies")
    
    def __str__(self):
        return "{} 영화에 {} 가 쓴 평점".format(self.movie_id.title, self.user_id.username)