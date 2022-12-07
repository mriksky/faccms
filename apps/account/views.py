from django.contrib.auth.models import Group
from account.models import User
from rest_framework import viewsets,permissions
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from account import serializers
from account import filter
from rest_framework.response import Response
from rest_framework.decorators import action

"""
1、获取对象信息
2、创建序列化器
3、转换数据
"""


class LocalTokenObtainPairView(TokenObtainPairView):
    """本地账户jwt登录视图 """
    serializer_class = serializers.LocalTokenObtainPairSerializer

class LocalTokenRefreshPairView(TokenRefreshView):
    """自定义JWT刷新视图"""
    serializer_class = serializers.LocalTokenRefreshPairSerializer

class UserViewSet(viewsets.ModelViewSet):
    # 通用的数据集
    queryset = User.objects.all().order_by('-date_joined')
    # 通用的序列化器
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.UserSerializer

    # 获取个人信息
    @action(methods=['GET'], detail=False)
    def owner(self, request):
        queryset = User.objects.get(pk=request.user.id)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=200)

class GroupViewSet(viewsets.ModelViewSet):
    ''' 用户组视图 '''
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.GroupSerializer
    queryset = Group.objects.order_by('-id')
    filterset_class = filter.GroupFilter
    ordering_fields = ('id',)







