from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    扩展用户表
    """
    SEX_CHOOSE = (
        ('0', '女'),
        ('1', '男'),
        ('2', '保密'),
    )

    realname = models.CharField(max_length=50, verbose_name='真实姓名')
    age = models.CharField(max_length=3, verbose_name='年龄')
    gander = models.CharField(max_length=2, choices=SEX_CHOOSE, default='2')
    phone = models.CharField(max_length=11, unique=True, null=True, blank=True, verbose_name='手机号码')
    avatar = models.ImageField(null=True, blank=True, verbose_name='头像')

    class Meta:
        db_table = 'auth_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.realname

# class UserInfo(models.Model):
#    '''
#         用户信息表
#    '''
#    SEX_CHOOSE = (
#        ('0', '女'),
#        ('1', '男'),
#        ('2', '保密'),
#    )
#
#    gander = models.CharField(max_length=2, choices=SEX_CHOOSE, default='2')
#    age = models.CharField(max_length=3, verbose_name='年龄')
#
#    class Meta:
#        db_table = 'auth_user_info'
#        verbose_name = '用户信息表'
