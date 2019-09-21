from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from api.serializers.users import UserSerializer, LoginSerializer
from api.serializers.clients import ClientSerializer
from api.models import User, Clients, Account, Loans, Transactions
from api.serializers.serializer_main import AccountSerializer, LoanSerializer, TransactionSerializer


class UserView(ModelViewSet):
    permission_classes = (AllowAny, )
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LoginView(APIView):
    permission_classes = (AllowAny, )
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientsView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = ClientSerializer
    queryset = Clients.objects.all()


class AccountView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class LoansView(ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = LoanSerializer
    queryset = Loans.objects.all()


class TransactionsView(ReadOnlyModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = TransactionSerializer
    queryset = Transactions.objects.all()
