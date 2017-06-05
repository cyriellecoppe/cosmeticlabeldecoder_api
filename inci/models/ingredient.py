from django.db import models


class Ingredient(models.Model):

    name = models.CharField(
        max_length=200,
        verbose_name='INCI name',
        unique=True,
    )

    common_name = models.CharField(
        max_length=200,
        blank=True,
    )

    description = models.CharField(
        max_length=400,
        verbose_name='Additional information',
        blank=True,
    )

    is_biodegradable = models.BooleanField(
        verbose_name='Biodegradable',
        default=False,
    )

    is_vegetable = models.BooleanField(
        verbose_name='Vegetable',
        default=False,
    )

    is_mineral = models.BooleanField(
        verbose_name='Mineral',
        default=False,
    )

    is_chemical = models.BooleanField(
        verbose_name='Chemical',
        default=False,
    )

    is_petrochemical = models.BooleanField(
        verbose_name='Petrochemical',
        default=False,
    )

    PRODUCTION_COST_CHOICES = (
        (1, 'low'),
        (2, 'mid'),
        (3, 'high'),
    )

    production_cost = models.IntegerField(
        choices=PRODUCTION_COST_CHOICES,
        default=PRODUCTION_COST_CHOICES[0][0],
    )

    types = models.ManyToManyField(
        'Type',
        related_name='ingredients',
    )

    @property
    def quality_price_ratio(self):
        # Ratio from 1/3 to 3/1
        ratio = round(self.environmental_score / self.production_cost, 2)
        # Convert ratio scale (from 1 to 3)
        return round((ratio + 2/3) * (3 / (3 + (2/3))), 2)

    @property
    def environmental_score(self):
        if (
            (self.is_vegetable or self.is_mineral)
            and (not self.is_petrochemical and not self.is_chemical)
        ):
            return 3
        elif (
            (not self.is_vegetable and not self.is_mineral)
            and (self.is_petrochemical or self.is_chemical)
        ):
            return 1
        else:
            return 2

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
