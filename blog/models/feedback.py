from django.core import validators
from django.db import models


class Feedback(models.Model):

    first_name = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            validators.RegexValidator(
                r'^[- \w]+$',
                "Enter a valid 'slug' consisting of Unicode letters, numbers, underscores, or hyphens.",
                'invalid'
            ),
        ],
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        validators=[
            validators.RegexValidator(
                r'^[- \w]+$',
                "Enter a valid 'slug' consisting of Unicode letters, numbers, underscores, or hyphens.",
                'invalid'
            ),
        ],
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    email = models.EmailField()

    comment = models.TextField()

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email
