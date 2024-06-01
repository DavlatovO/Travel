from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from .models import Carrier, Hotel, Travel


class TravelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    date = serializers.DateField()
    total_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    carrier_id = serializers.IntegerField()
    hotel_id = serializers.IntegerField()

    def create(self, validated_data):
        return Travel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.date = validated_data.get('date', instance.date)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.carrier_id = validated_data.get('carrier_id', instance.carrier_id)
        instance.hotel_id = validated_data.get('hotel_id', instance.hotel_id)
        instance.save()
        return instance


class CarrierSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)

    def create(self, validated_data):
        return Carrier.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('total_price', instance.price)
        instance.save()
        return instance

class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stars = serializers.IntegerField()

    def create(self, validated_data):
        return Hotel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stars = validated_data.get('stars', instance.stars)

