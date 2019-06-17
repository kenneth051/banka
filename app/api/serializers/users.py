from rest_framework import serializers
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    class Meta:
        model=User
        fields=[
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "password",
            "is_superuser",
            "is_active",
            "date_joined",
            "last_login",
            "gender",
        ]
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user     

