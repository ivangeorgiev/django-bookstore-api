from rest_framework import serializers

from . import models


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Publisher
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = models.Book
        fields = "__all__"
