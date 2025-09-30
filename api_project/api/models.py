from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)  # title field
    author = models.CharField(max_length=100)  # author field

    def __str__(self):
        return f"{self.title} by {self.author}"
