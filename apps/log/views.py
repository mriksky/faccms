from rest_framework import viewsets,permissions
from log import serializers
from log import filter
from log import models


class LoginLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.LoginLogSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = filter.LoginLogFilter
    ordering_fields = ('id',)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.LoginLog.objects.order_by('-id')
        else:
            return models.LoginLog.objects.filter(user=self.request.user).order_by('-id')

