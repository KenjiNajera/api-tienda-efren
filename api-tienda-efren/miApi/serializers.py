from rest_framework import serializers

from .models import producto

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = producto
        fields = ('id','nombre', 'precio')