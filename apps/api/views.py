from rest_framework import viewsets
from apps.api.serializers import ProductSerializer
from apps.api.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
