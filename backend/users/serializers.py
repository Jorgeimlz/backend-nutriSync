from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'password', 'age', 'gender', 
            'weight', 'height', 'dietary_preference', 'dietary_goal', 'is_staff'
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            age=validated_data.get('age'),
            gender=validated_data.get('gender'),
            weight=validated_data.get('weight'),
            height=validated_data.get('height'),
            dietary_preference=validated_data.get('dietary_preference'),
            dietary_goal=validated_data.get('dietary_goal'),
            is_staff=validated_data.get('is_staff', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
