from django.db import models

class Asset(models.Model):
    """资产信息"""
    VENDOR_CHOICES = (
        (1, '腾讯云'),
        (2, '阿里云'),
        (3, '华为云'),
        (4, '优刻云'),
    )
    TYPE_CHOICES = (
        (1, '服务器'),
        (2, '数据库'),
    )
    vendor = models.IntegerField(choices=VENDOR_CHOICES, verbose_name="云服务商")
    type = models.IntegerField(choices=TYPE_CHOICES, verbose_name="资产类型")
    ip = models.GenericIPAddressField(verbose_name="内网IP")
    vip = models.GenericIPAddressField(null=True, blank=True, verbose_name="公网IP")
    cpu = models.SmallIntegerField(verbose_name="CPU核数")
    memory = models.SmallIntegerField(verbose_name="内存容量")
    disk = models.SmallIntegerField(verbose_name="硬盘容量")
    version = models.CharField(max_length=64, verbose_name="系统版本")
    region = models.CharField(max_length=64, verbose_name="所属地域")
    uuid = models.CharField(unique=True, max_length=128, verbose_name="资产ID")

    def __str__(self):
        return self.ip

    class Meta:
        db_table = 'cmdb_asset'
        verbose_name = '资产信息'
        verbose_name_plural = verbose_name

class InventoryGroup(models.Model):
    """清单主机组信息"""
    project = models.CharField(max_length=32, verbose_name="项目名称")
    name = models.CharField(max_length=32, verbose_name='主机组名称')
    desc = models.CharField(max_length=32, verbose_name='主机组描述')
    vars = models.TextField(null=True, blank=True, verbose_name="主机组变量")

    def __str__(self):
        return self.desc + '_' + self.name

    class Meta:
        db_table = 'vars_group'
        unique_together = ['project', 'name']
        verbose_name = '主机组'
        verbose_name_plural = verbose_name

class InventoryHost(models.Model):
    """清单主机信息"""
    ENVIRONMENT_CHOICES = (
        (1, '正式环境'),
        (2, '测试环境'),
        (3, '提审环境')
    )
    region = models.CharField(max_length=32, verbose_name="项目大区")
    env = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=2, verbose_name="项目环境")
    group = models.ForeignKey(InventoryGroup, on_delete=models.PROTECT, verbose_name="主机属组")
    asset = models.ForeignKey(Asset, on_delete=models.PROTECT, verbose_name="主机资产")
    name = models.CharField(max_length=32, verbose_name='主机名称')
    desc = models.CharField(max_length=32, verbose_name='主机描述')
    used = models.BooleanField(default=True, verbose_name="是否启用")
    vars = models.TextField(null=True, blank=True, verbose_name="主机变量")

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vars_host'
        unique_together = ['region', 'env', 'group', 'name']
        verbose_name = '主机变量信息'
        verbose_name_plural = verbose_name

class InventoryVars(models.Model):
    """清单公共变量信息"""
    ENVIRONMENT_CHOICES = (
        (1, '正式环境'),
        (2, '测试环境'),
        (3, '提审环境')
    )
    region = models.CharField(max_length=32, verbose_name="项目大区")
    env = models.CharField(choices=ENVIRONMENT_CHOICES, max_length=2, verbose_name="项目环境")
    vars = models.TextField(null=True, blank=True, verbose_name="变量参数")

    def __str__(self):
        return '_'.join([str(self.region), str(self.env)])

    class Meta:
        db_table = 'vars_vars'
        unique_together = ['region', 'env']
        verbose_name = '公共变量信息'
        verbose_name_plural = verbose_name
