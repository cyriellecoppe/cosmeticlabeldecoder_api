from statistics import mean

from django.db import models
from django.db.models import Avg


class Product(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.CharField(
        max_length=200,
        blank=True,
    )

    PRICE_RANGE_CHOICES = (
        (1, 'low range'),
        (2, 'mid range'),
        (3, 'top range'),
    )

    price_range = models.IntegerField(
        choices=PRICE_RANGE_CHOICES,
        default=PRICE_RANGE_CHOICES[0][0],
    )

    brand = models.ForeignKey(
        'Brand',
        on_delete=models.PROTECT,
        related_name='products',
    )

    categories = models.ManyToManyField(
        'Category',
        related_name='products',
    )

    certifications = models.ManyToManyField(
        'Certification',
        related_name='products',
    )

    ingredients = models.ManyToManyField(
        'Ingredient',
        related_name='products',
    )

    image = models.ImageField(
        upload_to='products/',
        blank=True,
    )

    @property
    def price_score(self):
        ingredients_avg_cost = self.ingredients.aggregate(
            Avg('production_cost')
        )['production_cost__avg']
        # Ratio from 1/3 to 3/1
        price_ratio = round(ingredients_avg_cost / self.price_range, 2)
        # Convert ratio scale (from 1 to 3)
        return round((price_ratio + 2/3) * (3 / (3 + (2/3))), 2)

    @property
    def environmental_score(self):
        # from 1 (chemical) to 3 (natural): based on the environmental
        # score of each ingredient
        return round(
            mean(ingredient.environmental_score
                for ingredient in self.ingredients.all()),
            2)

    @property
    def is_biodegradable(self):
        return all(self.ingredients.values_list('is_biodegradable', flat=True))

    @property
    def quality_price_ratio(self):
        # Ratio from 1/3 to 3/1
        ratio = round((self.environmental_score / self.price_range), 2)
        # Convert ratio scale (from 1 to 3)
        return round((ratio + 2/3) * (3 / (3 + (2/3))), 2)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s %s' % (self.name, self.brand,)
