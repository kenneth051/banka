# Third-Party Imports
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter
from api.views import UserView

router = SimpleRouter()
router.register("users",UserView,"users")

urlpatterns = [
]

urlpatterns += router.urls
