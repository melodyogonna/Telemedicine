from rest_framework import serializers

from usermanager.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """Serializer for custom user model"""

    class Meta:
        model = CustomUser
        fields = '_all_'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
