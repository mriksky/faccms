from django_filters import rest_framework as filters
from . import models
from  django.contrib.auth.models import Group


class GroupFilter(filters.FilterSet):
    # icontains在ORM中表示不区分大小的包含
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Group
        fields = []
