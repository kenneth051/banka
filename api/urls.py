# Third-Party Imports
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import UserView, ClientsView, LoginView

router = SimpleRouter()
router.register("users",UserView,"users")
router.register("clients", ClientsView,"clients")

urlpatterns = [
    path('users/login/', LoginView.as_view()),
]

urlpatterns += router.urls
