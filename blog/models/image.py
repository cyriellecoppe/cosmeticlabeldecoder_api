from django.db import models


class Image(models.Model):

    title = models.CharField(
        max_length=100,
    )

    image = models.ImageField(
        upload_to='blog',
    )

    article = models.ForeignKey(
        'Article',
        on_delete=models.PROTECT,
        related_name='images',
    )

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
