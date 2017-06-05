from rest_framework import serializers

from .models import Brand
from .models import Category
from .models import Certification
from .models import Ingredient
from .models import Product
from .models import Type


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'image',
            'quality_price_ratio',
        )


class BrandSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Brand
        fields = (
            'id',
            'name',
            'products',
        )


class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'products',
        )


class CertificationSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Certification
        fields = (
            'id',
            'name',
            'description',
            'year_of_creation',
            'country_of_creation',
            'logo',
            'products',
        )


class IngredientSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'quality_price_ratio',
            'environmental_score',
            'products',
        )


class TypeSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Type
        fields = (
            'id',
            'name',
            'ingredients',
        )


class DetailedIngredientSerializer(serializers.ModelSerializer):

    products = ProductSerializer(
        read_only=True,
        many=True,
    )

    types = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True,
    )

    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
            'common_name',
            'description',
            'is_biodegradable',
            'is_vegetable',
            'is_mineral',
            'is_chemical',
            'is_petrochemical',
            'quality_price_ratio',
            'production_cost',
            'environmental_score',
            'types',
            'products',
        )


class DetailedProductSerializer(serializers.ModelSerializer):

    brand = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    categories = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
        many=True,
    )

    ingredients = IngredientSerializer(
        read_only=True,
        many=True,
    )

    certifications = CertificationSerializer(
        read_only=True,
        many=True
    )

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price_range',
            'price_score',
            'environmental_score',
            'quality_price_ratio',
            'is_biodegradable',
            'image',
            'brand',
            'ingredients',
            'categories',
            'certifications',
        )
