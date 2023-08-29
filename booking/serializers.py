from django.forms import model_to_dict
from rest_framework import serializers

from .models import Booking


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
