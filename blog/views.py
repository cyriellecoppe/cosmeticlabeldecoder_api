import django_filters
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from rest_framework.authentication import SessionAuthentication
from rest_framework import filters
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets

from .models import Article
from .models import Feedback
from .models import Image
from .models import News
from .models import Subscription

from .serializers import ArticleSerializer
from .serializers import FeedbackSerializer
from .serializers import ImageSerializer
from .serializers import NewsSerializer
from .serializers import SubscriptionSerializer


class ArticleFilter(django_filters.rest_framework.FilterSet):
    date = django_filters.NumberFilter(name='date', lookup_expr='year')

    class Meta:
        model = Article
        fields = ['date', 'id', ]


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('date',)
    filter_class = ArticleFilter


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class NewsFilter(django_filters.rest_framework.FilterSet):
    date = django_filters.NumberFilter(name='date', lookup_expr='year')

    class Meta:
        model = News
        fields = ['date', 'id', ]


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = (filters.OrderingFilter, filters.DjangoFilterBackend,)
    ordering_fields = ('date',)
    filter_class = NewsFilter


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class FeedbackAPI(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        email_to = serializer.validated_data['email']
        html_email_template = get_template('blog/email_feedback.html')
        context = {
            'created_at': serializer.instance.created_at,
            'comment': serializer.instance.comment,
        }
        html_email = html_email_template.render(context)
        mail_recipients = [email_to]
        if not settings.DEBUG:
            mail_recipients += [admin[1] for admin in settings.ADMINS]
        send_mail(
            'Cosmetic Label Decoder Feedback',
            'Thank you for your feedback',
            settings.EMAIL_HOST_USER,
            mail_recipients,
            fail_silently=False,
            html_message=html_email,
        )


class SubscriptionAPI(generics.CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def perform_create(self, serializer):
        super().perform_create(serializer)
        email_to = serializer.validated_data['email']
        html_email_template = get_template('blog/email_subscription.html')
        context = {
            'latest_news': News.objects.order_by('-date')[:3],
            'unsubscribe_token': serializer.instance.token,
        }
        html_email = html_email_template.render(context)
        send_mail(
            'Cosmetic Label Decoder Newsletter',
            'Thank you for your subscription',
            settings.EMAIL_HOST_USER,
            [email_to],
            fail_silently=False,
            html_message=html_email,
        )


def unsubscribe_email(request, token):
    subscription = get_object_or_404(Subscription, token=token)
    subscription.delete()
    return HttpResponse('Successfully unsubscribed.')
