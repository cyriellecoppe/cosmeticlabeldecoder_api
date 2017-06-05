from django.test import TestCase

from ..models import Brand
from ..models import Category
from ..models import Ingredient
from ..models import Product
from ..models import Type


class IngredientTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.almond = Ingredient(
            name='ALMOND',
            is_vegetable=True,
            is_mineral=True,
            is_petrochemical=True,
            is_chemical=True,
            production_cost=2,
        )

        cls.aloe = Ingredient(
            name='ALOE',
            production_cost=1,
        )

        cls.anise = Ingredient(
            name='ANISE',
            is_vegetable=True,
            is_mineral=True,
            is_petrochemical=True,
            production_cost=3,
        )

        cls.argan = Ingredient(
            name='ARGAN',
            is_vegetable=True,
            is_mineral=True,
            production_cost=1,
        )

        cls.linalool = Ingredient(
            name='LINALOOL',
            is_mineral=True,
            production_cost=2,
        )

        cls.sodium = Ingredient(
            name='SODIUM',
            is_petrochemical=True,
            production_cost=3,
        )

        cls.carbomer = Ingredient(
            name='CARBOMER',
            is_petrochemical=True,
            is_chemical=True,
            production_cost=1,
        )

    def test_environmental_score(self):
        self.assertEqual(self.almond.environmental_score, 2)
        self.assertEqual(self.aloe.environmental_score, 2)
        self.assertEqual(self.anise.environmental_score, 2)
        self.assertEqual(self.argan.environmental_score, 3)
        self.assertEqual(self.linalool.environmental_score, 3)
        self.assertEqual(self.sodium.environmental_score, 1)
        self.assertEqual(self.carbomer.environmental_score, 1)

    def test_ingredient_quality_price_ratio(self):
        self.assertEqual(self.almond.quality_price_ratio, 1.36)
        self.assertEqual(self.aloe.quality_price_ratio, 2.18)
        self.assertEqual(self.anise.quality_price_ratio, 1.09)
        self.assertEqual(self.argan.quality_price_ratio, 3)
        self.assertEqual(self.linalool.quality_price_ratio, 1.77)
        self.assertEqual(self.sodium.quality_price_ratio, 0.82)
        self.assertEqual(self.carbomer.quality_price_ratio, 1.36)


class ProductTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        b = Brand.objects.create(name='WELEDA')
        c = Category.objects.create(name='HAIR')
        t = Type.objects.create(name='EMULSIFIER')

        cls.almond = Ingredient.objects.create(
            name='ALMOND',
            is_biodegradable=True,
            is_vegetable=True,
            production_cost=1,
        )
        cls.almond.types.add(t)

        cls.anise = Ingredient.objects.create(
            name='ANISE',
            is_biodegradable=False,
            is_vegetable=True,
            is_petrochemical=True,
            production_cost=2,
        )
        cls.anise.types.add(t)

        cls.argan = Ingredient.objects.create(
            name='ARGAN',
            is_biodegradable=True,
            is_mineral=True,
            production_cost=3,
        )
        cls.argan.types.add(t)

        cls.linalool = Ingredient.objects.create(
            name='LINALOOL',
            is_biodegradable=False,
            is_chemical=True,
            production_cost=3,
        )
        cls.linalool.types.add(t)

        cls.cream = Product.objects.create(
            name='CREAM',
            price_range=1,
            brand=b,
        )
        cls.cream.categories.add(c)
        cls.cream.ingredients.add(cls.almond)
        cls.cream.ingredients.add(cls.argan)

        cls.soap = Product.objects.create(
            name='SOAP',
            price_range=2,
            brand=b,
        )
        cls.soap.categories.add(c)
        cls.soap.ingredients.add(cls.anise)
        cls.soap.ingredients.add(cls.linalool)

        cls.gel = Product.objects.create(
            name='GEL',
            price_range=3,
            brand=b,
        )
        cls.gel.categories.add(c)
        cls.gel.ingredients.add(cls.almond)
        cls.gel.ingredients.add(cls.anise)

        cls.paste = Product.objects.create(
            name='PASTE',
            price_range=3,
            brand=b,
        )
        cls.paste.categories.add(c)
        cls.paste.ingredients.add(cls.argan)
        cls.paste.ingredients.add(cls.linalool)

    def test_price_score(self):
        self.assertEqual(self.cream.price_score, 2.18)
        self.assertEqual(self.soap.price_score, 1.57)
        self.assertEqual(self.gel.price_score, 0.95)
        self.assertEqual(self.paste.price_score, 1.36)

    def test_composition_score(self):
        self.assertEqual(self.cream.environmental_score, 3)
        self.assertEqual(self.soap.environmental_score, 1.5)
        self.assertEqual(self.gel.environmental_score, 2.5)
        self.assertEqual(self.paste.environmental_score, 2)

    def test_is_biodegradable(self):
        self.assertTrue(self.cream.is_biodegradable)
        self.assertFalse(self.gel.is_biodegradable)
        self.assertFalse(self.soap.is_biodegradable)

    def test_product_quality_price_ratio(self):
        self.assertEqual(self.cream.quality_price_ratio, 3)
        self.assertEqual(self.soap.quality_price_ratio, 1.16)
        self.assertEqual(self.gel.quality_price_ratio, 1.22)
        self.assertEqual(self.paste.quality_price_ratio, 1.09)
