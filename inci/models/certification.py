from django.db import models


class Certification(models.Model):

    name = models.CharField(
        max_length=100,
        unique=True,
    )

    description = models.CharField(
        max_length=400,
        blank=True,
    )

    year_of_creation = models.IntegerField(
        verbose_name='Year of creation (YYYY)',
    )

    country_of_creation = models.CharField(
        max_length=100,
        blank=True,
    )

    logo = models.ImageField(
        upload_to='certifications/',
        blank=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s %s %s' % (
            self.name,
            self.year_of_creation,
            self.country_of_creation,
        )
