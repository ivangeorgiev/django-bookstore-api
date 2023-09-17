from django.db.models import Prefetch
from rest_framework import mixins, viewsets

from . import models, serializers

SWAGGER_TAGS = ["customers"]


class AddressViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    swagger_tags = SWAGGER_TAGS
    queryset = models.Address.objects.prefetch_related("country")
    serializer_class = serializers.AddressSerializer


class CustomerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    swagger_tags = SWAGGER_TAGS
    queryset = models.Customer.objects.prefetch_related("addresses", Prefetch("addresses__country"))
    serializer_class = serializers.CustomerSerializer
