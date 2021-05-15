from rest_framework import serializers
from . import models


class DateSerializer(serializers.Serializer):
    day = serializers.CharField(max_length=50)
    pk = serializers.IntegerField(read_only=True)
    def create(self, validated_data):
        day = validated_data.get('day')
        return models.Date.objects.create(day=day)



    def update(self, instance, validated_data):
        day = validated_data.get('day', instance.day)
        instance.day = day
        instance.save()
        return instance

