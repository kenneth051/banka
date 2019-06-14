# Third-Party Imports
from django.conf.urls import include
from django.urls import path
from rest_framework.routers import SimpleRouter



class OptionalSlashRouter(SimpleRouter):
    def __init__(self, trailing_slash="/?"):
        self.trailing_slash = trailing_slash
        super(SimpleRouter, self).__init__()


router = OptionalSlashRouter()

urlpatterns = [
]

urlpatterns += router.urls
