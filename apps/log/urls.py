from . import views
from rest_framework import routers

# 配置应用路由
router = routers.DefaultRouter()

router.register(r'api/login/log', views.LoginLogViewSet, basename='log')





