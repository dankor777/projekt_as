from django.db import models
from django.contrib.auth.models import User, Group
from django.urls import reverse

class Post(models.Model):
    tytul = models.CharField(max_length=255)
    tresc = models.TextField()
    id_autora = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.tytul + ' | ' + str(self.id_autora)
    def get_absolute_url(self):
        return reverse('index')

# class Role(models.Model):
#     nazwa = models.CharField(max_length=255, unique=True)
#     opis = models.TextField()

class Komentarz(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    tytul = models.CharField(max_length=255)
    tresc = models.TextField()
