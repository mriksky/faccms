from account.views import UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.SimpleRouter()

router.register(r'api/users', UserViewSet, basename='users')
router.register(r'api/groups', GroupViewSet, basename='groups')


#urlpatterns = []





