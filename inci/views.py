import django_filters
from rest_framework import filters
from rest_framework import viewsets

from .models import Brand
from .models import Category
from .models import Certification
from .models import Ingredient
from .models import Product
from .models import Type

from .serializers import BrandSerializer
from .serializers import CategorySerializer
from .serializers import CertificationSerializer
from .serializers import DetailedIngredientSerializer
from .serializers import IngredientSerializer
from .serializers import DetailedProductSerializer
from .serializers import ProductSerializer
from .serializers import TypeSerializer


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)


class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)


class DetailedIngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = DetailedIngredientSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    filter_fields = ('id',)


class IngredientFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(
        name='name',
        lookup_expr='istartswith',
    )

    class Meta:
        model = Ingredient
        fields = ['name', ]


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    filter_class = IngredientFilter


class DetailedProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = DetailedProductSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    filter_fields = ('id',)


class ProductFilter(django_filters.rest_framework.FilterSet):
    name = django_filters.CharFilter(
        name='name',
        lookup_expr='istartswith',
    )

    class Meta:
        model = Product
        fields = ['name', ]


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('name',)
    filter_class = ProductFilter


class TypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('name',)
