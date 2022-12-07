from django.contrib import admin
from account.models import User


class UserAccountAdmin(admin.ModelAdmin):
    admin.site.register(User)
