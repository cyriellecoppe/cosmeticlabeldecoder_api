from rest_framework import serializers

from .models import Article
from .models import Feedback
from .models import Image
from .models import News
from .models import Subscription


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = (
            'image',
            'title',
        )


class ArticleSerializer(serializers.ModelSerializer):

    images = ImageSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Article
        fields = (
            'id',
            'title',
            'date',
            'summary',
            'description',
            'images',
        )


class NewsSerializer(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    class Meta:
        model = News
        fields = (
            'id',
            'title',
            'date',
            'summary',
            'description',
            'category',
        )


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = (
            'first_name',
            'last_name',
            'email',
            'comment',
        )


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = (
            'email',
        )
