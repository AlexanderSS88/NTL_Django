from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name']


class AdvertisementSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True,)
    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'creator',
                  'status', 'created_at', 'updated_at', 'favor_users']

    def create(self, validated_data):
        validated_data['creator'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        adv = super().update(instance, validated_data)
        validated_data["creator"] = self.context["request"].user
        return adv

    def validate(self, data):
        if Advertisement.objects.filter(
                creator=self.context["request"].user,
                status='OPEN'
                ).count() >= 10:
            raise ValidationError(
                "You have more than 10 open advertisements"
                )
        return data
