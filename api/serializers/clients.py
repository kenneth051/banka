# from rest_framework import serializers
from api.models import Clients, Account
from api.serializers import BaseSerializer
from .serializer_main import AccountSerializer
from rest_framework import serializers

class ClientSerializer(BaseSerializer):
    account=serializers.SerializerMethodField()

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
            "image",
            "account",
        )
    def get_account(self,obj):
        account=Account.objects.filter(client=obj.id)
        info=AccountSerializer(account, many=True)
        return info.data
            
