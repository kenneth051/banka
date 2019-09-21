# Third-Party Imports
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import UserView, ClientsView, LoginView, AccountView, LoansView, TransactionsView

class OptionalSlashRouter(SimpleRouter):
    def __init__(self, trailing_slash="/?"):
        self.trailing_slash = trailing_slash
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

router.register("users",UserView,"users")
router.register("clients", ClientsView,"clients")
router.register("accounts", AccountView,"accounts")
router.register("loans", LoansView,"loans")
router.register("transactions", TransactionsView,"transactions")


urlpatterns = [
    path('users/login/', LoginView.as_view()),
]

urlpatterns += router.urls
