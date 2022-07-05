from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=250)
    description = serializers.CharField()
    price = serializers.IntegerField()
