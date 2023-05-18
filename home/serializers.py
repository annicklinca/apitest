from rest_framework import routers, serializers, viewsets
from .models import * 

# create user


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=('__all__') 