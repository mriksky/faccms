from rest_framework import serializers
from . import models
from utils.exception import APIException

import os
import re
import yaml
import csv



class AssetSerializer(serializers.ModelSerializer):
    """序列化资产信息"""
    class Meta:
        model = models.Asset
        fields = '__all__'

    # 自定义序列化输出格式
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["vendor"] = {"id": instance.vendor, "name": instance.get_vendor_display()}
        ret["type"] = {"id": instance.type, "name": instance.get_type_display()}
        return ret


class InventoryGroupSerializer(serializers.ModelSerializer):
    """序列化管理员清单主机组信息"""
    class Meta:
        model = models.InventoryGroup
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["project"] = {"id": instance.project.id, "name": instance.project.name}
        return ret


class InventoryGroupReadSerializer(serializers.ModelSerializer):
    """序列化普通用户清单主机组信息"""
    class Meta:
        model = models.InventoryGroup
        fields = ['id', 'desc']


class InventoryHostSerializer(serializers.ModelSerializer):
    """序列化清单主机信息"""
    class Meta:
        model = models.InventoryHost
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["region"] = {"id": instance.region.id, "name": str(instance.region)}
        ret["env"] = {"id": instance.env.id, "name": str(instance.env)}
        ret["group"] = {"id": instance.group.id, "name": str(instance.group)}
        ret["asset"] = {"id": instance.asset.id, "ip": instance.asset.ip}
        return ret


class InventoryVarsSerializer(serializers.ModelSerializer):
    """序列化清单变量信息"""
    class Meta:
        model = models.InventoryVars
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret["region"] = {"id": instance.region.id, "name": str(instance.region)}
        ret["env"] = {"id": instance.env.id, "name": str(instance.env)}
        return ret

class UploadHostVarsSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=32, label='上传文件')

    class Meta:
        model = models.InventoryVars
        fields = ['file', 'region', 'env']
        extra_kwargs = {
            'file': {'write_only': True}
        }

    def validate(self, attrs):
        fileName = attrs['file'].name
        if re.fullmatch(r'[A-z0-9_.-]+', fileName) is None:
            raise APIException("文件名格式错误,仅允许数字或字母或下划线或横杠")
        # 限制文件上传的文件类型
        ext = os.path.splitext(fileName)[1]
        valid_extensions = ['.yaml']
        if not ext.lower() in valid_extensions:
            raise APIException("上传的文件后缀不允许，请上传yaml格式")
        # 设置属性
        try:
            attrs['vars'] = yaml.load(attrs['file'].file)
        except Exception:
            raise APIException(detail='上传的yaml格式错误')
        del attrs['file']
        #attrs['file'] = attrs['file'].file
        print(attrs)
        return attrs

    # def create(self, validated_data):
    #    file = validated_data.pop('file')
    #    #vars_data= yaml.load(file)
    #    vars_collection = models.InventoryVars.objects.create(**validated_data, vars=vars_data)
    #    return vars_collection

    def to_representation(self, instance):
        return {
            'region': instance.region,
            'env': instance.env,
            'vars': instance.vars
        }

class UploadcsvSerializer(serializers.ModelSerializer):
    file = serializers.FileField(max_length=32, label='上传文件')

    class Meta:
        model = models.Asset
        fields = '__all__'
        extra_kwargs = {
            'file': {'write_only': True}
        }

    def validate(self, attrs):
        fileName = attrs['file'].name
        if re.fullmatch(r'[A-z0-9_.-]+', fileName) is None:
            raise APIException("文件名格式错误,仅允许数字或字母或下划线或横杠")
        # 限制文件上传的文件类型
        ext = os.path.splitext(fileName)[1]
        valid_extensions = ['.csv']
        if not ext.lower() in valid_extensions:
            raise APIException("上传的文件后缀不允许，请上传csv格式")
        # 设置属性
        #attrs['file'] = attrs['file'].file
        print(attrs)
        return attrs


    def create(self, validated_data):
        try:
            csv_file = (validated_data.pop('file'), 'r')
            with csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    print(row)
                    csv_data = {"vendor": row['VENDOR'], "type": row['资源类型'], "ip": row['主IPv4内网IP'],
                                "vip": row['主IPv4公网IP'], "cpu": row['CPU(核数)'], "memory": row['内存(GB)'],
                                "disk": {"system_disk": row['系统盘大小(GB)', "mount_disk": row['数据盘_0_大小（GB）']]},
                                "version": row['操作系统'],"region": row['地域'], "uuid": row['ID'],
                    }
                    csv_collection = models.Asset.objects.create(**validated_data)
            print(validated_data)
            return csv_collection
        except Exception:
            raise APIException(detail='解析的csv格式错误')

    def to_representation(self, instance):
        pass