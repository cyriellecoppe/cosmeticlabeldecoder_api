from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet
from .views import FeedbackAPI
from .views import ImageViewSet
from .views import NewsViewSet
from .views import SubscriptionAPI
from .views import unsubscribe_email


router = DefaultRouter()

router.register(r'articles', ArticleViewSet)
router.register(r'images', ImageViewSet)
router.register(r'news', NewsViewSet)


urlpatterns = router.urls + [
    url(r'^subscription/$', SubscriptionAPI.as_view(), name='subscription'),
    url(r'^unsubscribe/(?P<token>.*)/$', unsubscribe_email, name='unsubscribe'),
    url(r'^feedback/$', FeedbackAPI.as_view(), name='feedback'),
]
