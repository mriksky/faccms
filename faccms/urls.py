"""faccms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from account.views import LocalTokenObtainPairView, LocalTokenRefreshPairView
from rest_framework_simplejwt.views import TokenVerifyView
from utils.router import DefaultRouter


from account.urls import router as user_router
from log.urls import router as log_router
from cmdb.urls import router as cmdb_router

router = DefaultRouter()



# 1、创建路由对象
router.extend(user_router)
router.extend(log_router)
router.extend(cmdb_router)


urlpatterns = [
    # REST API 接口
    path('', include(router.urls)),
    path('api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', LocalTokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh', LocalTokenRefreshPairView.as_view(), name='token_refresh'),
    path('api/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    path('admin/', admin.site.urls),
]

# 合并所有路由
#urlpatterns += router.urls

