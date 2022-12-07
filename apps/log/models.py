from django.db import models
from account.models import User


class LoginLog(models.Model):
    """
    登录日志表
    """
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ipaddr = models.GenericIPAddressField()

    def __str__(self):
        return self.user.realname

    class Meta:
        db_table = 'login_log'
