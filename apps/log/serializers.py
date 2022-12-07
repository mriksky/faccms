from rest_framework import serializers
from log import models
from utils.ipParse import ip2addr

class LoginLogSerializer(serializers.ModelSerializer):
    """  """

    class Meta:
        model = models.LoginLog
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['user'] = instance.user.realname
        ret['ipaddress'] = ip2addr(ret['ipaddr'])
        return ret

