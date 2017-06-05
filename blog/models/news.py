from django.db import models


class News(models.Model):

    title = models.CharField(
        max_length=100,
        unique=True,
    )

    date = models.DateField(db_index=True)

    summary = models.CharField(
        max_length=300,
    )

    description = models.TextField()

    category = models.ForeignKey(
        'inci.Category',
        on_delete=models.PROTECT,
        related_name='news'
    )

    class Meta:
        ordering = ['title']
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
