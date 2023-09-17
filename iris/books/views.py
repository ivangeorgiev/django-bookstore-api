from rest_framework import mixins, viewsets

from . import models, serializers

SWAGGER_TAGS = ["books"]


class PublisherViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    swagger_tags = SWAGGER_TAGS
    queryset = models.Publisher.objects.all()
    serializer_class = serializers.PublisherSerializer


class AuthorViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    swagger_tags = SWAGGER_TAGS
    queryset = models.Author.objects.all()
    serializer_class = serializers.AuthorSerializer


class BookViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    swagger_tags = SWAGGER_TAGS
    queryset = models.Book.objects.prefetch_related("authors", "publisher", "language")
    serializer_class = serializers.BookSerializer
