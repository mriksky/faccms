from . import models
from django_filters import rest_framework as filters

class AssetFilter(filters.FilterSet):
    uuid = filters.CharFilter(field_name='uuid', lookup_expr='icontains', label='资产ID')

    class Meta:
        model = models.Asset
        fields = ['vendor', 'type', 'ip', 'vip']

class InventoryGroupFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='project__name', lookup_expr='icontains', label='项目名称')

    class Meta:
        model = models.InventoryGroup
        fields = ['project']

class InventoryHostFilter(filters.FilterSet):
    """过滤清单主机信息"""
    project = filters.CharFilter(field_name='region_project', label='项目ID')
    asset_ip = filters.CharFilter(field_name='asset_ip', lookup_expr='icontains', label='资产IP')

    class Meta:
        model = models.InventoryHost
        fields = ['region', 'env', 'group']


class InventoryVarsFilter(filters.FilterSet):
    """过滤清单变量信息"""
    project = filters.CharFilter(field_name='region_project', label='项目ID')

    class Meta:
        model = models.InventoryVars
        fields = ['region', 'env']


class UploadVarsFileFilter(filters.FilterSet):
    """过滤上传文件信息"""
    file = filters.CharFilter(field_name='file', lookup_expr='icontains', label='文件名称')
    date = filters.DateTimeFromToRangeFilter(label='上传时间<时间格式: 2020-01-01 10:00>')

    class Meta:
        model = models
        fields = []


