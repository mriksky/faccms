from . import views
from rest_framework import routers


# 配置应用路由
router = routers.SimpleRouter()


router.register(r'api/cmdb/asset', views.AssetViewSet, basename='asset')
router.register(r'api/cmdb/upload', views.UploadHostVarsViewSet, basename='upload')

#urlpatterns = []