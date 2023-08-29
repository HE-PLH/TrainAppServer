from django.forms import model_to_dict
from rest_framework import serializers

from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"

        # fields = ["id", "title", date, "description", "images"]

    def update(self, instance, validated_data):
        instance.start = validated_data.get("start", instance.start)
        instance.end = validated_data.get("end", instance.end)
        instance.from_station = validated_data.get("from_station", instance.from_station)
        instance.to_station = validated_data.get("to_station", instance.to_station)
        instance.train = validated_data.get("train", instance.train)


        instance.save()
        return instance
