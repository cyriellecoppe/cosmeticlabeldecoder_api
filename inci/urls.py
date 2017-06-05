from rest_framework.routers import DefaultRouter

from .views import BrandViewSet
from .views import CategoryViewSet
from .views import CertificationViewSet
from .views import DetailedIngredientViewSet
from .views import DetailedProductViewSet
from .views import IngredientViewSet
from .views import ProductViewSet
from .views import TypeViewSet


router = DefaultRouter()

router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'certifications', CertificationViewSet)
router.register(r'detailedingredient', DetailedIngredientViewSet, base_name='detailed-ingredient')
router.register(r'ingredients', IngredientViewSet)
router.register(r'detailedproduct', DetailedProductViewSet, base_name='detailed-product')
router.register(r'products', ProductViewSet)
router.register(r'types', TypeViewSet)

urlpatterns = router.urls
