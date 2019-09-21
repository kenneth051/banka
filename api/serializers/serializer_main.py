from rest_framework import serializers
from api.serializers import BaseSerializer
from api.models import Account, Loans, Transactions


class AccountSerializer(BaseSerializer):
    class Meta:
        model = Account
        fields=("id", "created_on", "added_by", "client", "balance")

class LoanSerializer(BaseSerializer):
    class Meta:
        model= Loans
        fields=("id", "created_on", "added_by","client_account","amount","interest","time_category","time")


class TransactionSerializer(BaseSerializer):
    class Meta:
        model= Transactions
        fields=("id", "created_on", "added_by","client_account","amount","loan","action")
