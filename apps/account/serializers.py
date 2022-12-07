from django.contrib.auth.models import Group
from account import models
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from django.contrib.auth.hashers import make_password
from datetime import datetime
from faccms import settings
import re


class LocalTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''本地账户jwt token 认证方法  '''

    # 重写validate方法
    def validate(self, attrs):
        # 过期时间
        ACCESS_EXPIRY_TIME = int((datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']).timestamp())
        # 刷新时间
        REFRESH_EXPIRY_TIME = int((datetime.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']).timestamp())

        data = super().validate(attrs)
        data['id'] = self.user.id
        data['access_exp'] = ACCESS_EXPIRY_TIME
        data['refresh_exp'] = REFRESH_EXPIRY_TIME
        print(data)
        return data


class LocalTokenRefreshPairSerializer(TokenRefreshSerializer):
    '''
    本地账户jwt token 刷新方法
    '''

    # 重写validate方法
    def validate(self, attrs):
        # 过期时间
        ACCESS_EXPIRY_TIME = int((datetime.now() + settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME']).timestamp())
        # 刷新时间
        REFRESH_EXPIRY_TIME = int((datetime.now() + settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']).timestamp())

        data = super().validate(attrs)
        data['access_exp'] = ACCESS_EXPIRY_TIME
        data['refresh_exp'] = REFRESH_EXPIRY_TIME
        print(data)
        return data


class GroupSerializer(serializers.ModelSerializer):
    #  继承于serializers.ModelSerializer（模型序列化器）
    # user_set = serializers.PrimaryKeyRelatedField(many=True, queryset=models.User.objects.all(), write_only=True)
    user_set = serializers.StringRelatedField(read_only=True, many=True)

    # 用以对模型的字段进行序列化

    class Meta:
        # 指定要序列化的模型
        model = Group
        fields = ['id', 'name', 'user_set']
        read_only_fields = ['user_set']

class UserSerializer(serializers.ModelSerializer):
    """  用户序列化 """
    groups = GroupSerializer(read_only=True, many=True)
    last_login = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)

    class Meta:
        model = models.User
        fields = ['id', 'username', 'password', 'realname', 'is_superuser', 'is_staff', 'phone', 'email', 'last_login',
                  'groups']
        # 指定序列化只读字段
        read_only_fields = ['username', 'is_superuser', 'last_login']
        # 序列化附加关键字参数
        extra_kwargs = {
            'username': {'max_length': 30, 'min_length': 4, 'trim_whitespace': True},
            'password': {'write_only': True, 'min_length': 8, 'trim_whitespace': True},
            'realname': {'min_length': 2, 'trim_whitespace': True},
            'phone': {'max_length': 11, 'min_length': 11},
        }
    # 字段级别验证 方法名固定格式validate_字段
    def validate_phone(self, value):
        if not re.match(r'^1[358]\d{9}$|^147\d{8}$|^176\d{8}$', value):
            raise serializers.ValidationError("手机号码格式错误")
        else:
            return value

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        validated_data['password'] = make_password(validated_data['password'])
        return super().update(instance, validated_data)

