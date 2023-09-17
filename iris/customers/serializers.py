from rest_framework import serializers

from . import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        fields = "__all__"
        model = models.Address


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        fields = "__all__"
        model = models.Customer
