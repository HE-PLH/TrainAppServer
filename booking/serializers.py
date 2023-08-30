from django.forms import model_to_dict
from rest_framework import serializers

from .models import Booking, BookingItem


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "title", date, "description", "images"]

    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.images = validated_data.get("images", instance.images)

        instance.save()
        return instance


class BookingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookingItem
        fields = "__all__"
        image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
        # fields = ["id", "title", date, "description", "images"]

    def update(self, instance, validated_data):
        instance.booking = validated_data.get("booking", instance.booking)
        instance.schedule = validated_data.get("schedule", instance.schedule)
        instance.seats = validated_data.get("seats", instance.seats)

        instance.save()
        return instance
