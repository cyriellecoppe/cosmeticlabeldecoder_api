from django.db import models


class Article(models.Model):

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    date = models.DateField(db_index=True)

    summary = models.TextField()

    description = models.TextField()

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
