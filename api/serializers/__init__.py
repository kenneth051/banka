from rest_framework import serializers
from api.models import Clients


class BaseSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data):
        user = self.context["request"].user
        data["added_by"] = user.id
        data = super().to_internal_value(data)
        return data
