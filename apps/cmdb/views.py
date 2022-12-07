from . import models
from . import serializers, filter
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated


class AssetViewSet(viewsets.ModelViewSet):
    """管理资产信息"""
    serializer_class = serializers.AssetSerializer
    queryset = models.Asset.objects.order_by('vendor')
    permission_classes = (IsAuthenticated,)
    filterset_class = filter.AssetFilter
    ordering_fields = ('id',)


class InventoryGroupViewSet(viewsets.ModelViewSet):
    """管理清单主机组信息"""
    queryset = models.InventoryGroup.objects.order_by('project')
    filterset_class = filter.InventoryGroupFilter
    permission_classes = (IsAuthenticated,)
    ordering_fields = ('id',)

class InventoryHostViewSet(viewsets.ModelViewSet):
    """管理清单主机信息"""
    serializer_class = serializers.InventoryHostSerializer
    queryset = models.InventoryHost.objects.order_by('region')
    permission_classes = (IsAuthenticated,)
    filterset_class = filter.InventoryHostFilter
    ordering_fields = ('id',)


class InventoryVarsViewSet(viewsets.ModelViewSet):
    """管理清单变量信息"""
    serializer_class = serializers.InventoryVarsSerializer
    queryset = models.InventoryVars.objects.order_by('region')
    permission_classes = (IsAuthenticated,)
    filterset_class = filter.InventoryVarsFilter
    ordering_fields = ('id',)


class UploadHostVarsViewSet(viewsets.ModelViewSet):
    """上传vars变量文件视图"""
    parser_classes = [MultiPartParser]
    serializer_class = serializers.UploadHostVarsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = models.InventoryVars.objects.order_by('-id')

    # def perform_create(self, serializer):
    #     pass