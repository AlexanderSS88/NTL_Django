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
        quantity = Advertisement.objects.filter(
                creator=self.context["request"].user,
                status='OPEN'
                ).count()
        if self.context['request'].method in ['POST'] and quantity >= 10:
            raise ValidationError(
                "You have more than 10 open advertisements"
                )
        elif ((self.context['request'].method in ['PATCH'])
              and (quantity >= 10)
              and ('status' in data)):
            if data['status'] == 'OPEN':
                raise ValidationError(
                    "You have more than 10 open advertisements"
                )
        return data
