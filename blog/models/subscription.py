import secrets
from django.db import models


def generate_token():
    return secrets.token_urlsafe(128)


class Subscription(models.Model):

    email = models.EmailField(
        unique=True,
    )

    token = models.TextField(
        default=generate_token,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email
