from . import models
from django_filters import rest_framework as filters


class LoginLogFilter(filters.FilterSet):
    """过滤用户登录信息"""
    realname = filters.CharFilter(field_name='user__realname', lookup_expr='icontains')

    class Meta:
        model = models.LoginLog
        fields = []