from rest_framework import serializers
from api.models import Clients

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clients
        fields = (
            "id",
            "client_name",
            "email" ,
            "occupation",
            "address",
            "gender",
            "contact",
            "added_by",
            "image"
        )
    def to_internal_value(self, data):
        user=self.context["request"].user
        data["added_by"]=user.id
        data = super().to_internal_value(data)
        return data

