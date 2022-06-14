from rest_framework import serializers
from base.models import Item
from base.models import Price

class PriceSerializer(serializers.ModelSerializer):
    # prices = serializers.SlugField()
    class Meta:
        model= Price
        fields=('price_stock', 'created')

class ItemSerializer(serializers.ModelSerializer):
    prices=PriceSerializer(many=True)
    class Meta:
        model=Item
        fields='__all__'

